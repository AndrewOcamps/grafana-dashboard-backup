import os
import requests
import json
import yaml
from datetime import datetime

def get_dashboard_list(key, host):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    url = host + '/api/search/'
    headers = {'Authorization' : key}
    r = requests.get(url=url, headers=headers)

    if r.status_code == 200:
        dashboard_list = r.json()
        uid_list = []
        for dashboard in dashboard_list:
            uid_list.append(dashboard['uid'])
        return uid_list
    else:
        return '{} ERROR: HTTP {} {}'.format(time, r.status_code, url)

def backup_dashboard(uid, key, host, path):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    backup_dir = path
    url = host + '/api/dashboards/uid/' + uid
    headers = {'Authorization' : key}
    r = requests.get(url=url, headers=headers)

    if r.status_code == 200:
        dashboard_json = r.json()

        meta = dashboard_json['meta']
        #version = meta['version']
        #url = meta['url']
        #created = meta['created']
        #createdBy = meta['createdBy']
        #updated = meta['updated']
        #updatedBy = meta['updatedBy']
        slug = meta['slug']

        dashboard = dashboard_json['dashboard']
        dashboard_path = backup_dir + '/' + slug + '.json'
        try:
            with open(dashboard_path, 'w') as f:
                json.dump(dashboard, f)
        except EnvironmentError:
            return '{} ERROR: fail to export {}'.format(time, slug)
        
        return '{} SUCCESS: {}'.format(time, slug)
    else:
        return '{} ERROR: HTTP {} {}'.format(time, r.status_code, url)


if __name__ == "__main__":
        
    configuration = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.yml')

    with open(configuration, 'r') as f:
        try:
            config = yaml.safe_load(f)
            host = config['host']
            backup_dir = config['backup_path']

            for org in config['organization']:
                path = os.path.join(backup_dir, str(org['name']))
                key = org['key']
                if not os.path.exists(path):
                    os.makedirs(path)
                
                for uid in get_dashboard_list(key, host):
                    print(backup_dashboard(uid, key, host, path))

        except yaml.YAMLError as err:
            print(err)



    
