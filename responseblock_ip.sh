#!/bin/bash

IP=$1

sudo iptables -A INPUT -s $IP -j DROP

echo "$(date) - Blocked IP: $IP" >> logs/security.log