#!/bin/bash

SERVICE="nginx"

if ! systemctl is-active --quiet $SERVICE
then
    systemctl restart $SERVICE
    echo "$(date) - $SERVICE restarted" >> logs/security.log
fi