import signupFlow.test_val as val
import requests

params = ()
cookies = {
    'eigi-geolocated-country-code': 'us',
    'currency': 'INR',
    'Currency_Symbol': '\xE2\x82\xB9',
    'country': 'IND',
    'Currency': 'INR',
    'custid': val.custid,
    'admin_user': val.admin_user,
    'port2083': 'no',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


if val.hosting_plan == 'shared':
    params = (
        ('cpanel_plan', val.specific_plan),
    )
elif val.hosting_plan == 'eCommerce':
    params = (
        ('flow', ['woocommerce', '']),
        ('cpanel_plan', val.specific_plan),
    )

response = requests.get('https://www.beta.bluehost.in/web-hosting/signup', headers=headers, params=params, cookies=cookies)
print(response.text)
