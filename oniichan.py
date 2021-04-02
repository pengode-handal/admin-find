#recode?  Sangaddddd cupuuuuuuuuuuu, recode cupu kli,  ga menghargai _-
#mengimportan bahan
from __future__ import print_function
import sys
import time
import os
import time
import socket

    
# by BabwaXgura
print("install bahan dulu")
time.sleep(1)
os.system('pip install requests')
os.system('pip3 install -r bahan.txt')
time.sleep(1)
import requests
import asyncio
import aiohttp
from aiohttp import ClientSession
time.sleep(0.3)
os.system('clear')
time.sleep(1)
#buli version
if sys.version[0] in "2":
    print ("\n[x] bang ga bisa di python 2 python 1 bisanya awokawok makanya liat dulu perintahnya:v \n")
    print ("\n\n\thmmm \033[1;91mI heker kok termos? \033[0mawokawok canda bang\n\n")
    exit()

#system warna

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

from requests import Session
s = Session()

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
def mediumprint(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
def fastprint(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 170)
def cepet(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 200)
        

#loding
slowprint('[!] Starting : ')
time.sleep(2)
os.system('clear')

cepet(""" \033[92m \n
           _              __ _           _
  __ _  __| |_ __ ___    / _(_)_ __   __| | ___ _ __
 / _` |/ _` | '_ ` _ \  | |_| | '_ \ / _` |/ _ \ '__|
| (_| | (_| | | | | | | |  _| | | | | (_| |  __/ |
 \__,_|\__,_|_| |_| |_| |_| |_|_| |_|\__,_|\___|_|
 """);
fastprint (""" \33[94m \n
########################################################
* author by : BabwaXgura     team:Muslim Cyber Anonymous
* coded by : BabwaXgura      thanks to: Allah,member MCA
* version : 1.2.0            tools: admin finder
########################################################
""")
print('\n [+] ohayou/oyasumi/moshi moshi oniichan')
print('\n [+] tools ini 100℅ work nii chan')
print('\n [+] gunakan tools dengan bijak wahai heker\n')
time.sleep(2)
print('\n [!] note : gausah pake https/http, langsung domainya')
#memulai masukan target
target = input("\33[93;1m \n masukan target url=> \33[1;0m")
print("")
#mengecek prokotol
target = target.replace('https://', '')
target = target.replace('http://', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target



#define variables, functions, etc.
start = time.time()

yay = []

conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    ) 
#men scanning
async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status #mengecek responding website
        if status == 200:
            print("\33[97;1mpew (>O_O)>  \33[1;0m{}\33[97;1m  <(O_O<) pew {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1mga ketemu \33[94;1m{}\33[91;1m 404 {}".format(response.url, status))
        elif status == 403:
            print("\33[91;1mforbidden \33[94;1m{}\33[91;1m 403 \33[95;1m{}".format(response.url, status))
        else:
            print("\33[95;1m??? {} ??? {}".format(response.url, status))
        return await response.read()
#membuka list direktori
async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('list_dir.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)

    async with ClientSession(connector=conn) as session: #creates the tasks
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
        
#start loop        
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)

#mengeluarkan hasil
end = time.time()
script_time = end - start
print("\33[93;1mWaktu scanning butuh {} detik untuk selesai\n".format(script_time))
print("\33[91;1m### \33[93;1mnih hasilnya \33[91;1m###\33[1;0m")
if len(yay) == 0:
    print("\33[94;1m!!! NO RESULTS !!!")
else:
    for y in yay:
        print(y)    
print("\33[91;1m###############")
