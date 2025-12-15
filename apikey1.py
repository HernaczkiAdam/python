import requests

url = "https://api.thecatapi.com/v1/breeds"
headers = {
    "x-api-key": "DEMO_API_KEY"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Hiba történt, státuszkód:", response.status_code)
