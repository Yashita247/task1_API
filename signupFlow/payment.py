import requests
import json
from signupFlow.test_val import admin_user, custid, domain_name, domain_action

tax_json_dict = {}

def tax():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.beta.bluehost.in',
        'Connection': 'keep-alive',
    }

    data = '{"user_info":{"country":"IN","city":"Mumbai","zip":"400063","address":"NESCO IT Park, Western Express Highway","state":"MH",' \
           '"cust_id":"'+custid+'","lastname":"Jain","currency":"INR"},"products":[{"sku":"286227ce","term":"36"}]}'

    response = requests.post('https://my.beta.bluehost.in/api/tax_estimate', headers=headers, data=data, verify = True)
    return response.text

def purchase(tax_json):
    tax_json_dict = json.loads(tax_json)
    print(tax_json_dict['tax'])
    cookies = {
        'eigi-geolocated-country-code': 'us',
        'currency': 'INR',
        'Currency_Symbol': '\xE2\x82\xB9',
        'country': 'IND',
        'Currency': 'INR',
        'custid': custid,
        'admin_user': admin_user,
        'port2083': 'no',
        'ir': 'house%5EHOMEPAGEBYPASS%5Ehttps%3A%2F%2Fwww.beta.bluehost.in%2Fweb-hosting%2Fsignup%3Fcpanel_plan%3Dbasic',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.beta.bluehost.in',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    data = {
        'session_id_3ds': '',
        'access_token': '',
        'brand': 'bluehost_in',
        'c': '',
        'card_secret': '',
        'card_token': '',
        'card_token_creator': '',
        'card_token_data': '',
        'card_token_mask': '',
        'cc_id': '',
        'cc_type': '',
        'continue_anyway': '',
        'currency': 'INR',
        'cust_id': custid,
        'cvv2_secret': '',
        'data': '53616c7465645f5fa7a901bdd26eb97843c32cc2ca5b7abf8d2ed0f3bd4d42dae65fff413e6026c1cf8ac3224e3653c76a92fe349d81f7ef42aac0f203178dd2c891c09eb666b4fb33c8ec8387480423938c0ed7361f71dc8d2b1c046422daca6a7782c18b01ba0524381621baad5ad53c4d0ce686b42836a51c8464e3e81f76fc43357f939743fd',
        'domain': domain_name,
        'domain_action': domain_action,
        'ir': 'house^HOMEPAGEBYPASS^https://www.beta.bluehost.in/web-hosting/signup?cpanel_plan=basic',
        'sso_provider': '',
        'sso_token': '',
        'sso_username': '',
        'sug_id': '',
        'tax_estimate': tax_json_dict["tax"],
        'tax_json': tax_json,
        'is_test_account': '1',
        'ctct_test_account': '1',
        'test_self_destruct': '0.04',
        'auto_fill_drop': '41xxxxxxxxxx1111 Approved',
        'experience': 'bluerock',
        'stockcpanel': 'stock',
        'paas_override_gateway_name': '--- Allow PaaS to pick the best option ---',
        'sku': '286227ce',
        'firstname': 'Yashita',
        'lastname': 'Jain',
        'company': 'Testing: Yashita.j Inc',
        'country': 'IN',
        'address': 'NESCO IT Park, Western Express Highway',
        'city': 'Mumbai',
        'state': 'MH',
        'zip': '400063',
        'phone_cc': '91',
        'phone': '18004194426',
        'phone_ext': '0',
        'email': 'yashita.j@endurance.com',
        'tax_type': 'india_gst',
        'tax_id': '',
        'term': 'cpanel:basic-36',
        'bd_test': '1',
        'paymethod': 'check',
        'check_number': '1234',
        'purchase_order': '',
        'tos_agree': 'yes'
    }

    response = requests.post('https://www.beta.bluehost.in/web-hosting/signup', headers=headers, cookies=cookies,
                             data=data)

    return response


tax_json = tax()
#print(tax_json)
purchase_res = purchase(tax_json)
print(purchase_res.text)
