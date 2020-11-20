#!/bin/bash
# Gerardo Ocampos

dir=$(echo $PWD) 

$dir/venv/bin/python backup.py > logs/backup_grafana-$(date +"%m-%d-%Y").log 2>&1
