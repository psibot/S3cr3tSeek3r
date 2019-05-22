#!/bin/bash
# SCRIPT:
# REV: Version 1.0
# PLATFORM: Linux
# AUTHOR: PSIBOT
#
# PURPOSE: Linux template
#
##########################################################
########### DEFINE FILES AND VARIABLES HERE ##############
##########################################################

##########################################################
################ BEGINNING OF MAIN #######################
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

clear
function pause(){
   read -p "$*"
}

echo -e "\e[40;38;5;82m S3cr3t \e[30;48;5;82m Seek3r\e[0m"
echo
echo -e  "\e[32m[+]\e[0m RUN ALL COMMANDS WITH SUDO! \e[0m"
echo -e  "\e[32m[+]\e[0m Firts open a new terminal And RUN1.sh this will setup a PROXY Server for own protection \e[0m"
echo -e  "\e[32m[+]\e[0m When RUN1.sh was executed open NEW terminal and run CHECKIP1.sh to confirm your new IP \e[0m"
echo -e  "\e[32m[+]\e[0m When ABOVE STEPS ARE COMPLETED , HIT ENTER .... ENJOY SEARCHING!!! \e[0m"
echo

pause 'Press [Enter] key to continue...'

sudo python infograb.py

####################################################
################ END OF MAIN #######################
####################################################
exit 0
# End of script
