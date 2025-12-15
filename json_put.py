import requests, json

d={
      "id": "11",
      "nev": "Flektor",
      "ar": 1200,
      "bekerulesiOrszag": "Hollandia",
      "gyartasiIdo": "2024-07-17"
    }

h={'Content-Type': 'application/json'}
valasz = requests.put("http://localhost:3000/gyogyszerek/11", headers=h, data=json.d>
print(valasz.status_code)
