import os

try:
    import requests
except:
    os.system('pip install requests')
    import requests

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent')
    from user_agent import generate_user_agent

try:
    from colorama import Fore,Style
except:
    os.system('pip install colorama')
    from colorama import Fore,Style

if os.name == 'nt':
    os.system('color')

os.system('cls' if os.name == 'nt' else 'clear')

import random
from time import sleep
x = requests.get('https://tinyurl.com/y6zohma3').text.splitlines()

class O0Dev():
    def __init__(self):
        self.done = 0
        self.bad = 0
        self.err = 0
        self.blc = 0
    
    def auto_users(self):
        print(Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        usersx = []
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.'
        user_len = int(input(Fore.LIGHTYELLOW_EX+"[+] Enter your user length : "))
        user_count = int(input("[+] How many users would you like : "))
        for x in range(0, user_count):
            users = ""
            for x in range(0, user_len):
                users_char = random.choice(chars)
                users = users + users_char
            usersx.append(users)
        for user in usersx:
            try:
                hed = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                    'cookie' : 's_v_web_id=verify_4759e77ec70b30f5809b99b4e83cf170; tt_csrf_token=UnnTT-BD3b77BER0ScMT23x9; tt_webid_v2=6972528352738199042; tt_webid=6972528352738199042; MONITOR_WEB_ID=6972528352738199042; csrf_session_id=33dd9ae2d7064521b1fb68c47fb6e376; ttwid=1%7CwLimK0e14CMaCXiLsX2myGQvJoR3fo915olavJk5Dj8%7C1623418284%7Ce18f90ac79a745872544fd1583a806821d5f6c9158b0d627195c391e1826811a; R6kq3TV7=AMcrRft5AQAAjVJfEPehKE83G62yRxwPcWPaXYFikZR7GX1aQHzgFfgvUVYW|1|0|2b554837c6bb50a519a30dbd9d5993dc6bc9a899; ak_bmsc=81F43ED7B422ED308CE38925766575B825EEFE85C4210000AE65C360177EFA1B~pl1L8RCHdpnfcXaxKe2pz/rrFGQ7AvIDfN7D/22TzpTU+jZhxDJTPJeeBqZzBzFebXtRYd+rf7S7OmBWLe/P+NNTeXnw6pCQxbC3oIFuwYRtUEK/JN2GEhm+/Aft3RoUgU4e/U9MIt7FtXUm521joEAelJCNASPG7sXkCL9Gquc/S7Ss/uOSbUow59iqm/DE20qw90c3qyotU354d2k5uT/ZtjaXyF1fKW5RtVkjiSo2o=; bm_sz=37D69FC94E991FC2E9B16E331298202E~YAAQhf7uJch1QPd5AQAAtjFF+wwIPFmp+JnukUWFwWqe7X7doAuSddcEaF98dBdy4UG5HI0g+qLiAFukmWs9uJR48l9ItBNHUpPwRrW2gnAfasr0c7zqprBzAMgrMT0jqPEG2GenpL5lp6psMYSUW2agxDZY++1VmDyejBjQGqRh/g4VVjEnSpZ1kTrkah0q; _abck=3BB0FC28EA3D19A3D635197B489889C5~-1~YAAQhf7uJcl1QPd5AQAAtjFF+wZF5KnpMJ3JntFWraZlabgy8zYpHCGWOOOlZvd9iDaNjP0aLxrOLfernQM/KlnKVqllWNtTsnVatlXA9uvEtOcTzhLFiEoynT/MfV6GtNEzx54dOdnFXliM7F0ifN4WMqNvlQddCjSTp4ESCxMCZ/wixpiJAj7fhh+lqObndimxpSyFkdDwKKL/2r+zoMxUTUz7vga3x19kWzjEHbFfRsUsKEsq8Kz945ZlHNTbYsGhuLJbYW7sfixqbGe5AnJcU+H/JwGPEgW3fCJiF7lWCaAm9zR6iwUoi6HfM4QlxsM2eNX0hXyFm75mwFrP5GDjVH5PWn9cpsoovHfhXb9cDwjlN2L0gvqUPCU=~-1~-1~-1',
                    'referer': f'https://www.tiktok.com/@{user}?lang=en',
                    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': generate_user_agent()
                }
                res = requests.get(f'https://www.tiktok.com/@{user}?lang=en',headers=hed).status_code

                if res == 200:
                    self.bad +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                elif res == 404:
                    searched = []
                    search = requests.get(f'https://api19-va.tiktokv.com/aweme/v1/search/sug/?keyword={user}&source=discover&history_list=%255B%255D&from_group_id=6955847075842067717&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=2021907040&dpi=240&carrier_region=IQ&uoo=0&region=US&app_name=musical_ly&version_name=19.7.4&timezone_offset=28800&ts=1623414125&ab_version=19.7.4&residence=IQ&cpu_support64=false&current_region=IQ&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2021907040&_rticket=1623414126984&device_platform=android&iid=6970768855900374790&build_number=19.7.4&locale=en&op_region=IQ&version_code=190704&timezone_name=Asia%2FShanghai&cdid=a599dba8-5eec-4478-a8cd-366f816af723&openudid=20b16e653809202b&sys_region=US&device_id=6948436704496682502&app_language=en&resolution=768*1366&device_brand=google&language=en&os_version=7.1.2&aid=1233&mcc_mnc=41840',headers={'User-Agent': 'okhttp/3.12.1'}).json()['sug_list']
                    for ls in search:
                        line = str(ls['content']).replace(' ','')
                        searched.append(line)

                    if str(user) in searched:
                        self.done +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                        good = open('good.txt','a',encoding='utf8').write(f'{user}\n')
                        try:
                            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=❖ TikTok : {user}\n❖ Free By : @O0Dev')
                        except:
                            pass
                    else:
                        self.bad +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                    searched.clear()
                else:
                    self.blc +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
            except Exception as d:
                #cc = open('dd.txt','a').write(f'{d}\n')
                self.err +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
    
    def use_list(self):
        print(Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        try:
            file = open('users.txt','r',encoding='utf8').read().splitlines()
        except:
            print(Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+'[!] users.txt Not Found In the same PATH !!')
            print(Style.RESET_ALL)
            sleep(3)
            quit()
        for user in file:
            try:
                hed = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                    'cookie' : 's_v_web_id=verify_4759e77ec70b30f5809b99b4e83cf170; tt_csrf_token=UnnTT-BD3b77BER0ScMT23x9; tt_webid_v2=6972528352738199042; tt_webid=6972528352738199042; MONITOR_WEB_ID=6972528352738199042; csrf_session_id=33dd9ae2d7064521b1fb68c47fb6e376; ttwid=1%7CwLimK0e14CMaCXiLsX2myGQvJoR3fo915olavJk5Dj8%7C1623418284%7Ce18f90ac79a745872544fd1583a806821d5f6c9158b0d627195c391e1826811a; R6kq3TV7=AMcrRft5AQAAjVJfEPehKE83G62yRxwPcWPaXYFikZR7GX1aQHzgFfgvUVYW|1|0|2b554837c6bb50a519a30dbd9d5993dc6bc9a899; ak_bmsc=81F43ED7B422ED308CE38925766575B825EEFE85C4210000AE65C360177EFA1B~pl1L8RCHdpnfcXaxKe2pz/rrFGQ7AvIDfN7D/22TzpTU+jZhxDJTPJeeBqZzBzFebXtRYd+rf7S7OmBWLe/P+NNTeXnw6pCQxbC3oIFuwYRtUEK/JN2GEhm+/Aft3RoUgU4e/U9MIt7FtXUm521joEAelJCNASPG7sXkCL9Gquc/S7Ss/uOSbUow59iqm/DE20qw90c3qyotU354d2k5uT/ZtjaXyF1fKW5RtVkjiSo2o=; bm_sz=37D69FC94E991FC2E9B16E331298202E~YAAQhf7uJch1QPd5AQAAtjFF+wwIPFmp+JnukUWFwWqe7X7doAuSddcEaF98dBdy4UG5HI0g+qLiAFukmWs9uJR48l9ItBNHUpPwRrW2gnAfasr0c7zqprBzAMgrMT0jqPEG2GenpL5lp6psMYSUW2agxDZY++1VmDyejBjQGqRh/g4VVjEnSpZ1kTrkah0q; _abck=3BB0FC28EA3D19A3D635197B489889C5~-1~YAAQhf7uJcl1QPd5AQAAtjFF+wZF5KnpMJ3JntFWraZlabgy8zYpHCGWOOOlZvd9iDaNjP0aLxrOLfernQM/KlnKVqllWNtTsnVatlXA9uvEtOcTzhLFiEoynT/MfV6GtNEzx54dOdnFXliM7F0ifN4WMqNvlQddCjSTp4ESCxMCZ/wixpiJAj7fhh+lqObndimxpSyFkdDwKKL/2r+zoMxUTUz7vga3x19kWzjEHbFfRsUsKEsq8Kz945ZlHNTbYsGhuLJbYW7sfixqbGe5AnJcU+H/JwGPEgW3fCJiF7lWCaAm9zR6iwUoi6HfM4QlxsM2eNX0hXyFm75mwFrP5GDjVH5PWn9cpsoovHfhXb9cDwjlN2L0gvqUPCU=~-1~-1~-1',
                    'referer': f'https://www.tiktok.com/@{user}?lang=en',
                    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': generate_user_agent()
                }
                res = requests.get(f'https://www.tiktok.com/@{user}?lang=en',headers=hed).status_code
                print(f'{user} -- {res}')
                if res == 200:
                    self.bad +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                elif res == 404:
                    searched = []
                    search = requests.get(f'https://api19-va.tiktokv.com/aweme/v1/search/sug/?keyword={user}&source=discover&history_list=%255B%255D&from_group_id=6955847075842067717&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=2021907040&dpi=240&carrier_region=IQ&uoo=0&region=US&app_name=musical_ly&version_name=19.7.4&timezone_offset=28800&ts=1623414125&ab_version=19.7.4&residence=IQ&cpu_support64=false&current_region=IQ&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2021907040&_rticket=1623414126984&device_platform=android&iid=6970768855900374790&build_number=19.7.4&locale=en&op_region=IQ&version_code=190704&timezone_name=Asia%2FShanghai&cdid=a599dba8-5eec-4478-a8cd-366f816af723&openudid=20b16e653809202b&sys_region=US&device_id=6948436704496682502&app_language=en&resolution=768*1366&device_brand=google&language=en&os_version=7.1.2&aid=1233&mcc_mnc=41840',headers={'User-Agent': 'okhttp/3.12.1'}).json()['sug_list']
                    for ls in search:
                        line = str(ls['content']).replace(' ','')
                        searched.append(line)

                    if str(user) in searched:
                        self.done +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                        good = open('good.txt','a',encoding='utf8').write(f'{user}\n')
                        try:
                            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=❖ TikTok : {user}\n❖ Free By : @O0Dev')
                        except:
                            pass
                    else:
                        self.bad +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
                    searched.clear()
                else:
                    self.blc +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')
            except Exception as d:
                #cc = open('dd.txt','a').write(f'{d}\n')
                self.err +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n[-] Good : {self.done}\n[-] Bad : {self.bad}\n[-] Blocked : {self.blc}\n[-] Error : {self.err}\n[-] {user}')

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = (Fore.LIGHTGREEN_EX+"""

  _____ _  __   ____   ___   __  ___          
 |_   _| |/ /  / __ \ / _ \ /  \|   \ _____ __
   | | | ' <  / / _` | (_) | () | |) / -_) V /
   |_| |_|\_\ \ \__,_|\___/ \__/|___/\___|\_/ 
               \____/                         
[-----------(Coded By : Osama A.M.Y)-----------]
        """)
        print(banner)
        try:
            print('[-] ',str(x[0]))
        except:
            pass
        opt = input(Fore.LIGHTYELLOW_EX+"""
[1] Check Users with auto users
[2] Check Users Using List
[3] Generate Users in users.txt

[+] Choice Ur Option : """)
        if opt == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            token = input('[+] Enter Tele Bot Token : ')
            ID = input('[+] Enter Tele User ID : ')
            print(Style.RESET_ALL)
            O0Dev().auto_users()
        elif opt == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            token = input('[+] Enter Tele Bot Token : ')
            ID = input('[+] Enter Tele User ID : ')
            print(Style.RESET_ALL)
            O0Dev().use_list()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            chars = 'abcdefghijklmnopqrstuvwxyz1234567890_'
            user_len = int(input("[+] Enter your user length : "))
            user_count = int(input("[+] How many users would you like : "))
            for x in range(0, user_count):
                users = ""
                for x in range(0, user_len):
                    users_char = random.choice(chars)
                    users = users + users_char
                file = open('users.txt','a',encoding='utf8').write(f'{users}\n')
            print('[-] Done Save Users in users.txt')
            sleep(3)

# Channel  @O0Dev
# Dev Tele @o_7ay
# Dev Inst @o.7ay