import requests
import os

API_KEY = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY", "INSIRA_SUA_CHAVE_AQUI")

def verificar_segurança_google(url):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + API_KEY
    body = {
        "client": {
            "clientId": "verificador",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        resp = requests.post(endpoint, json=body)
        data = resp.json()
        return {"seguro": not bool(data)}
    except:
        return {"seguro": False}