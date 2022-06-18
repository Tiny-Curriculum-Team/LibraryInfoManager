#!/usr/bin/env bash

CUR_PATH=$(cd "$(dirname "$0")"; pwd)

TASK_FREQUENCY=${2:-"*/30 * * * *"}
TASK_COMMAND="python Django/manage.py dumpdata > ./DataBackup/DataBackup_$(date +%Y%m%d_%H%M%S).json"
CRONTAB_TASK="${TASK_FREQUENCY} ${TASK_COMMAND}"
CRONTAB_BAK_FILE="${CUR_PATH}/crontab_bak"

echo $CRONTAB_TASK

function create_crontab()
{
    echo 'Creating crontab task...'
#    crontab -l > conf && echo "* * * * * hostname >> /tmp/tmp.txt" >> conf && crontab conf && rm -f conf
    crontab -l > ${CRONTAB_BAK_FILE} 2>/dev/null
    sed -i "/s*.*${TASK_COMMAND}/d" ${CRONTAB_BAK_FILE}  # 已存在任务时会被sed删除，防止重复添加
    echo "${CRONTAB_TASK}" >> ${CRONTAB_BAK_FILE}
    crontab ${CRONTAB_BAK_FILE}
    echo 'Completed!'
}

function clear_crontab(){
    echo 'Deleting crontab task...'
#    crontab -l | grep -v "python Django/manage.py dumpdata > ./DataBackup/DataBackup_" > conf
    crontab -l > ${CRONTAB_BAK_FILE} 2>/dev/null
    sed -i "/.*${SCRIPT_NAME}/d" ${CRONTAB_BAK_FILE}
    crontab ${CRONTAB_BAK_FILE}

    echo 'Completed!'
}

if [ $# -lt 1 ]; then
    echo "Usage: $0 [start | stop | manual] [*/30 * * * *]"
    echo "[* * * * *] Parameters are the same as crontab task frequency syntax."
    echo "If [* * * * *] doesn't exist, then the parameters will be [*/30 * * * *] by default."
    exit 1
fi

case $1 in
    'start' )
        create_crontab
        ;;
    'stop' )
        clear_crontab
        ;;
    'manual' )
        python Django/manage.py dumpdata > ./DataBackup/DataBackup_$(date +%Y%m%d_%H%M%S).json
esac
