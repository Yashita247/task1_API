import signupFlow.test_val as val
import requests

cookies = {
    'eigi-geolocated-country-code': 'us',
    'user_login': val.domain_name,
    'country': 'IND',
    'Currency': 'INR',
    'Currency_Symbol': '%26%238377%3B',
    'custid': val.custid,
    'port2083': 'no',
    'currency': 'INR',
    'admin_user': val.admin_user,
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://my.beta.bluehost.in',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

data = {
  'l_redirect': 'https://my.beta.bluehost.in/cgi-bin/cplogin?domain='+val.domain_name,
  'l_server_time': '1613157246',
  'l_expires_min': '0',
  'ldomain': val.domain_name,
  'lpass': val.password
}

response = requests.post('https://my.beta.bluehost.in/cgi-bin/cplogin', headers=headers, cookies=cookies, data=data)
print(response.text)