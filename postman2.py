import requests

user='postman'
passwd='password'
h={'Authorization': Basic 'cG9zdG1hbjpwYXNzd29yZA=='}
valasz = requests.get("https://postman-echo.com/basic-auth", auth=(user,passwd))
print(valasz.headers)
print (valasz.json())
print(valasz.status_code)
ez a postman2
