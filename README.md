
S3cr3tSeek3r V.1

Need to install (tested on Ubuntu)
* **Ubuntu**: ```$ sudo apt install gir1.2-appindicator3-0.1 gir1.2-notify-0.7 python-gobject curl whois geoip python3-dev  python-dev python3-bs4 python3-setuptools```

For OPENVPN Proxy !!!
* **openvpn**: ```$ sudo apt-get install openvpn```
* **python-requests**: ```$ sudo apt-get install python-requests```
* **python-urwid 1.3+**: ```$ sudo apt-get install python-urwid``` , for `tui` version (terminal user interface)
* **wmctrl**: ```$ sudo apt-get install wmctrl```, for `Indicator` of `tui` version, use for focusing window from indicator.

# How to use:
* !!!ALWAYS RUN ALL COMMANDS WITH SUDO!!!
* Execute  ```sudo ./S3cr3tSeek3r.sh ``` in terminal
* Then open a new terminal And  ```sudo ./RUN1.sh ``` this will setup a PROXY Server IP for own protection
* Next When RUN1.sh was executed open NEW terminal and run  ```sudo ./CHECKIP1.sh ``` to confirm your new IP
* When ABOVE STEPS ARE COMPLETED , HIT ENTER .... ENJOY SEARCHING!!!

* I have included a example of search, you can click on url's to open in browser... have fun!

![Example](https://i.imgur.com/mPlu4BV.png)


Also do :
https://gist.github.com/DusanMadar/c1155329cf6a71e4346cae271a2eafd3

Steps
1. Install and check Tor status
root@75f6721089f2:/# apt update
root@75f6721089f2:/# apt install tor
root@75f6721089f2:/# service tor status
 * tor is not running
2. Start Tor and check it's running
root@75f6721089f2:/# service tor start 
 * Starting tor daemon...          [ OK ] 
root@75f6721089f2:/# service tor status
 * tor is running
3. Try to Authenticate with nc (Netcat)
It's not possible to connect as ControlPort is not set yet.

root@75f6721089f2:/# apt install netcat
root@75f6721089f2:/# echo -e 'AUTHENTICATE' | nc 127.0.0.1 9051
(UNKNOWN) [127.0.0.1] 9051 (?) : Connection refused
4. Stop/kill Tor, set ControlPort and start Tor again
root@75f6721089f2:/# service tor stop
 * Stopping tor daemon...          [fail]
root@75f6721089f2:/# pidof tor | xargs kill
root@75f6721089f2:/# service tor status
 * tor is not running
root@75f6721089f2:/# echo "ControlPort 9051" >> /etc/tor/torrc
root@75f6721089f2:/# service tor start 
 * Starting tor daemon...          [ OK ] 
5. Try to Authenticate with nc again
It's possible to connect but Authentication fails.

root@75f6721089f2:/# echo -e 'AUTHENTICATE' | nc 127.0.0.1 9051
515 Authentication failed: Wrong length on authentication cookie.
6. Stop/kill Tor, turn off CookieAuthentication and start Tor again
root@75f6721089f2:/# service tor stop
 * Stopping tor daemon...          [fail]
root@75f6721089f2:/# pidof tor | xargs kill
root@75f6721089f2:/# echo "CookieAuthentication 0" >> /etc/tor/torrc
root@75f6721089f2:/# service tor start
 * Starting tor daemon...
Jan 20 11:34:30.911 [warn] ControlPort is open, but no authentication method has been configured. 
                           This means that any program on your computer can reconfigure your Tor.
                           That's bad!
                           You should upgrade your Tor controller as soon as possible.
                    [ OK ] 
7. Try to Authenticate with nc again
Authentication passes.

# NOTE Use Ctrl+C to exit.
root@75f6721089f2:/# echo -e 'AUTHENTICATE' | nc 127.0.0.1 9051
250 OK
8. Check your public IP and currently used Tor ip
root@75f6721089f2:/# apt install curl
root@75f6721089f2:/# curl http://icanhazip.com/ 
89.196.159.79
root@75f6721089f2:/# torify curl http://icanhazip.com/   
185.220.101.17
9. Change and check Tor IP
root@75f6721089f2:/# echo -e 'AUTHENTICATE\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
250 OK
250 OK
250 closing connection
root@75f6721089f2:/# torify curl http://icanhazip.com/
185.220.101.6
10. Change (with Python3) and check Tor IP
root@75f6721089f2:/# apt install python3
root@75f6721089f2:/# apt install python3-pip
root@75f6721089f2:/# pip3 install stem
root@75f6721089f2:/# python3
>>> from stem import Signal
>>> from stem.control import Controller
>>> 
>>> with Controller.from_port(port=9051) as controller:
...     controller.authenticate()
...     controller.signal(Signal.NEWNYM)
... 
>>> 
root@75f6721089f2:/# torify curl http://icanhazip.com/
185.107.81.233
