import requests, json

d={
      "id": "11",
      "nev": "Flektor",
      "ar": 1500,
      "bekerulesiOrszag": "Hollandia",
      "gyartasiIdo": "2024-07-17"
    }

h={'Content-Type': 'application/json'}
valasz = requests.post("http://localhost:3000/gyogyszerek/", headers=h, data=json.du>
#print(valasz.text)
print(valasz.status_code)
#print(valasz.headers)
