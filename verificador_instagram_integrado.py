
import requests
import json
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
import time

# --- MÉTODO DE COMPARAÇÃO COM GOOGLE ---
def verificar_nome_google(username):
    try:
        query = f"site:instagram.com {username}"
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('a')
        perfis = []

        for resultado in resultados:
            href = resultado.get('href')
            if href and "instagram.com" in href and "/p/" not in href:
                inicio = href.find("https://www.instagram.com/")
                if inicio != -1:
                    fim = href.find("/", inicio + 26)
                    perfil = href[inicio+26:fim if fim != -1 else None]
                    if perfil and perfil != username and perfil not in perfis:
                        perfis.append(perfil)
        return perfis
    except Exception as e:
        return []

# --- MÉTODO DE COMPARAÇÃO COM SCRAPERAPI ---
def verificar_com_scraperapi(username, api_key):
    try:
        url = f"http://api.scraperapi.com?api_key={api_key}&url=https://www.instagram.com/{username}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if "Page Not Found" in response.text or response.status_code == 404:
            return False
        return True
    except:
        return False

# --- MÉTODO DE COMPARAÇÃO COM APIFY ---
def verificar_com_apify(username, apify_token):
    try:
        url = f"https://api.apify.com/v2/acts/dtrungtin~instagram-profile-scraper/run-sync-get-dataset-items?token={apify_token}"
        payload = {
            "usernames": [username],
            "resultsLimit": 1
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        data = response.json()
        return isinstance(data, list) and len(data) > 0
    except:
        return False

# --- FUNÇÃO PRINCIPAL DE VERIFICAÇÃO COMPLETA ---
def verificar_perfil_completo(username, scraperapi_key, apify_key):
    resultados = {
        "existe_scraperapi": verificar_com_scraperapi(username, scraperapi_key),
        "existe_apify": verificar_com_apify(username, apify_key),
        "parecidos_google": verificar_nome_google(username),
        "parecidos_fuzzy": []
    }

    for similar in resultados["parecidos_google"]:
        ratio = fuzz.partial_ratio(username.lower(), similar.lower())
        if ratio >= 80:
            resultados["parecidos_fuzzy"].append(similar)

    return resultados
