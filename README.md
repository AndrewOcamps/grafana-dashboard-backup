# grafana-dashboard-backup
A simple python script to backup grafana dashboards via API

### Specify the url of your grafana

``` yaml
# Configuration File 'config.yml'
---
host: "http://hostname:3000"
backup_path: "./export"
```

### Specify the list of organizations configured in Grafana

``` yaml
# Configuration File 'config.yml'
---
organization:
  - name: 'Main Org.'
    key: 'Bearer eyJrIjoiT1paMnVkbFJibHRabmNxTTAwOUoyam9xS1dZZVZRN2UiLCJuIjoiYmFja3VwVXNlciIsImlkIjoxfQ=='
```

> *key*: is the authentication token that can be generated by following thIs documentation: [https://grafana.com/docs/grafana/latest/http_api/auth/](https://grafana.com/docs/grafana/latest/http_api/auth/)`

### Start the backup script by the following way
#### Using Python directly
> Requires python 3

_Install dependencies_
```
pip install -r requirements.txt
```
_Start the process and leave it running in the background_
```
python backup.py > logs/backup_grafana-$(date +"%m-%d-%Y").log 2>&1
```
#### Using Python with virtual environment
> Requires python 3 and virtualenv


_Initialize virtual environment_
```
virtualenv -p python3 venv
source venv/bin/activate
```

_Install dependencies_
```
(venv) pip install -r requirements.txt
```
_Start the process with a script_
```
(venv) ./run.sh
```

#### The script will export all the dashboards in json format inside the export directory. You can enter the directory and observe as follows. 

``` bash
.
├── export
│   └── Main Org.
│       ├── host-linux.json
│       ├── host-windows.json
│       ├── jboss-fuse.json
│       ├── oracledb.json
│       └── postgresql-db-connection.json
```
> In my case my organization is called Main Org. and all the dashboards associated with the organization are stored inside

#### You can observe any eventuality in the following log
``` bash
logs/backup_grafana-11-20-2020.log
20/11/2020 14:49:38 SUCCESS: host-linux
20/11/2020 14:49:38 SUCCESS: host-windows
20/11/2020 14:49:38 SUCCESS: jboss-fuse
20/11/2020 14:49:38 SUCCESS: oracledb
20/11/2020 14:49:38 SUCCESS: postgresql-db-connection
```

