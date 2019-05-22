#!/bin/bash
# SCRIPT:  myip.sh
# REV: Version 4.0
# PLATFORM: Linux
# AUTHOR: psibot
# PURPOSE: Info from your current IP
# CURL and WHOIS must be installed.
#
#
#
##########################################################
########### DEFINE FILES AND VARIABLES HERE ##############
##########################################################
clear

LOG_DIR=/var/log
ROOT_UID=0
LINES=50
E_XCD=86
E_NOTROOT=87

# Run as root, of course.
if [ "$UID" -ne "$ROOT_UID" ]
then
echo -e "\e[5m Must be root to run this script!"
exit $E_NOTROOT
fi
if [ -n "$1" ]
# Test whether command-line argument is present (non-empty).
then
lines=$1
else
lines=$LINES # Default, if not specified on command-line.
fi

echo -e "\e[31m __      __.__           .__         ._____________\e[25m"
echo -e "\e[33m/  \    /  \  |__   ____ |__| ______ |   \______   \e[25m"
echo -e "\e[32m\   \/\/   /  |  \ /  _ \|  |/  ___/ |   ||     ___/\e[25m"
echo -e "\e[31m \        /|   Y  (  <_> )  |\___ \  |   ||    |    \e[25m"
echo -e "\e[33m  \__/\  / |___|  /\____/|__/____  > |___||____|.v4\e[25m"
echo -e "\e[32m       \/       \/ psibot        \/             \e[25m \e[0m"
echo
date
echo
echo

echo -e  "Install all"
apt  install curl whois geoiplookup
clear

echo -e "\e[32m  !!!!!!!!!!!!!!!  \e[25m \e[0m"
echo -e "\e[32m  Starting APP \e[25m \e[0m"
echo -e "\e[32m  !!!!!!!!!!!!!!!  \e[25m \e[0m"
echo
echo -e "\e[4mYOUR Global IP is:\e[25m\e[0m "
curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//' > ip
echo
curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//'
echo
echo
echo

while read ip
do
     geoiplookup $ip
     echo
     echo " "
     echo -e "\e[32m  !!!!!!!!!!!!!!!  \e[25m \e[0m"
      echo -e "\e[32m  FucK The System  \e[25m \e[0m"
     echo -e "\e[32m  !!!!!!!!!!!!!!!  \e[25m \e[0m"
     echo
done<ip

rm ip

echo -e "\e[31mIf the IP is that you are connecting from"
echo -e "I suggest you look at TOR and OPENVPN"
echo -e "....THIS WILL KEEP YOU OUT OF JAIL"
echo -e "THIS IS THE TOOLS OF OUR TRADE\e[0m"

echo "Awake, arise or be for ever fall’n."
echo -e     "\e[31m― John Milton, Paradise Lost\e[0m"
echo
echo
echo
exit 0
