#!/usr/bin/env bash
python Django/manage.py dumpdata > ./DataBackup/DataBackup_$(date +%Y%m%d_%H%M%S).json
