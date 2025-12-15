import requests

keres = input("Kerj: ")
try:
        valasz = requests.get("http://localhost:3000/gyogyszerek" + keres)
except:
        print("Halozati hiba!")
        exit()

if valasz.status_code == 200:
        print (valasz.json())
print(valasz.status_code)
