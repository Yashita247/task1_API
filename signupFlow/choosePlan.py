from signupFlow.test_val import admin_user, hosting_plan
import requests

cookies = {
    'eigi-geolocated-country-code': 'us',
    'user_login': 'test-ypj04.com',
    'currency': 'INR',
    'Currency_Symbol': '\xE2\x82\xB9',
    'country': 'IND',
    'Currency': 'INR',
    'admin_user': admin_user,
    'port2083': 'no',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

if hosting_plan=='shared':
    response = requests.get('https://www.beta.bluehost.in/hosting/shared', headers=headers, cookies=cookies)
elif hosting_plan=='eCommerce':
    response = requests.get('https://www.beta.bluehost.in/wordpress/woocommerce-hosting', headers=headers, cookies=cookies)
print(response.text)
