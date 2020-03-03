#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

clear
gateway=$(route | awk '{if ($1 == "default"} print $2;')

echo "---------------------------"
echo "*** Beginning Test ***"
echo "3"
ping -c 2 $gateway > /dev/null; gateway_pinged=$?
echo "2"
ping -c 2 1.1.1.1 > /dev/null; remote_pinged=$?
echo '1'
ping -c 2 www.google.com > /dev/null; dns_resolved=$?

echo "Your gateway is $gateway"
if [ $gateway_pinged -eq 0 ]
then
    echo -e "Connection to default gateway is ${GREEN}SUCCESSFUL!${NC}"
else
    echo -e "Connection to default gateway ${RED}FAILED!${NC}"
fi

if [ $remote_pinged -eq 0 ]
then
    echo -e "Remote Connection ${GREEN}SUCCEDED!${NC}"
else
    echo -e "Remote Connection ${RED}FAILED!${NC}"
fi

if [ $dns_resolved -eq 0 ]
then
    echo -e "DNS resolution ${GREEN}SUCCEDED!${NC}"
else
    echo -e "DNS resolution ${GREEN}FAILED!${NC}"
fi
