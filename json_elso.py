import requests
eroforras = input("Adj meg egy eroforrast a szerveren: ")
valasz = requests.get("http://localhost:3000/gyogyszerek" + eroforras)
print(valasz.text)
print(valasz.status_code)
#print(valasz.headers)
