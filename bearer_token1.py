import requests

url = "https://api.thecatapi.com/v1/breeds"
headers = {
    "x-api-key": "DEMO_API_KEY"
}

valasz = requests.get(url, headers=headers)

if valasz.status_code == 200:
    print("Jo lekeres!")
    print(valasz.json())
else:
    print("Hiba tortent. HTTP statusz:", valasz.status_code)
