import requests
import re
from urllib.parse import urlparse

dict = []

def paymentScope(mainUrl):
        data = (urlparse(mainUrl).netloc).replace("https://", '').split('.')
        return mainUrl.replace("https://", '') if len(data) == 3 else f"www.{mainUrl}"

def get_str(string, start, end):
    string = ' ' + string
    ini = string.find(start)
    if ini == -1:
        return ''
    ini += len(start)
    end_index = string.find(end, ini)
    if end_index == -1:
        return ''
    length = end_index - ini
    return string[ini:ini+length].strip()

def multiexplode(delimiters, string):
    delimiters = "|".join(map(re.escape, delimiters))
    pattern = f'[{delimiters}]'
    return re.split(pattern, string)

def hit_sender_proxy(message):
    bot_token = '6792050074:AAEmyyjDK37ebW5ZL-YwDyERMKYVXPBkCiE'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': -4140245152, 'text': message}
    requests.post(url, data=data)


def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None



async def proxy_ip(porxylist,session):
    try:
        resp = await session.get("https://api.ipify.org")
        print(resp.text)

        if resp.status_code == 200 or 'Bad' in resp.text or 'Too' in resp.text:
            if porxylist not in dict:
                dict.append(porxylist)
                hit_sender_proxy(message=f"Proxy Live = {porxylist}")

        
        return resp.text
    except Exception as e:
        return e

def proxy_check(proxy):
    try:
        r1 = requests.get('https://api.ipify.org', proxies=proxy)
        if r1.status_code == 200 or 'Bad' in r1.text or 'Too' in r1.text:
            if proxy not in dict:
                dict.append(proxy)
                hit_sender_proxy( 'Live Proxy ✅ => '+str(proxy))
            return True
    except:
        return False
    
def GetStrX(s, start, end):
    return (s.split(start))[1].split(end)[0]