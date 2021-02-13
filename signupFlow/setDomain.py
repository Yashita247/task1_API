from signupFlow.test_val import admin_user,custid, domain_action, domain_name
import requests

cookies = {
    'eigi-geolocated-country-code': 'us',
    'currency': 'INR',
    'Currency_Symbol': '\xE2\x82\xB9',
    'country': 'IND',
    'Currency': 'INR',
    'custid': custid,
    'admin_user': admin_user,
    'port2083': 'no',
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
      'domain_action': domain_action,
      'currency': 'INR',
      'ir': 'house^manual^-',
      'c': '',
      'sku': 'e692108c',
      'show_header': '',
      'domain': domain_name,
      'tld': 'com'
    }

response = requests.post('https://www.beta.bluehost.in/web-hosting/signup', headers=headers, cookies=cookies, data=data)
print(response.text)