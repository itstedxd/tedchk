import asyncio,httpx
from fake_useragent import UserAgent
import random
# from apdefs import *
from api.defs import *
from api.Test import checks
from api.response_str import get_auth_resp
from flask import Blueprint, request
from .function import get_str, multiexplode, proxy_check, GetStrX, paymentScope
import requests
import time
import random
import string
import traceback
import base64
import json

api_bp4 = Blueprint('strip_ccn', __name__)

from api.function import proxy_ip

def multiexplode(s):
    return s.split(':')

@api_bp4.route('/strip_ccn')
async def sh():
    
    lista = request.args.get('lista')   
    telegram_hit_id = request.args.get("tg_id")
    porxylist = request.args.get('proxy')
    if not porxylist:
        return f'<br>CC: {lista if lista else ""}<br>Response: DEAD ❌ - ENTER THE PROXY IN THE PROXY BLOCK <br>'
    
    ip, port, user, pass1 = multiexplode(porxylist)
    mainpro = f'http://{user}:{pass1}@{ip}:{port}'
    proxy_dict = {'http://': mainpro, 'https://': mainpro}
    
    async with httpx.AsyncClient(timeout=120,follow_redirects=True,proxies=proxy_dict) as session:
       
            ip_address = await proxy_ip(porxylist,session)
            try:
                 response = await checks(lista,session)
                 peols = response.json()

                #  peols = await get_auth_resp(response,lista)

            except Exception as e:
                 peols = {
                      "status": "DEAD ❌",
                      "response": str(e),
                      "fullz": lista,
                    
                 }
            json_response = json.dumps(peols, ensure_ascii=False)


            return json_response





            # try:
            #     lol = await Fuck_shopi(session,lista,link="https://bluemercury.com/products/snow-fox-skincare-japanese-cherry-blossom-white-tea-smoothing-mask?variant=32787938803787")
            #     peols = await response_all_shopify(lista,lol,ip_address)
            # except Exception as e:
            #     peols= f"<br>CC: {lista if lista else ''}<br>Response: DEAD ❌ - {str(e)} <br>"


       
        


