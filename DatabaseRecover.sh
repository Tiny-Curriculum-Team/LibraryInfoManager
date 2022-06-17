#!/usr/bin/env bash
DataJsonFile="${1:-`ls -lt DataBackup | grep 'DataBackup_' | head -n 1 | awk '{print $8}'`}"
python Django/manage.py loaddata DataBackup/${DataJsonFile}