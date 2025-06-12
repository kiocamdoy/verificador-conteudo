
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import json
import time

# ScraperAPI
def verificar_via_scraperapi(username, api_key="YOUR_SCRAPERAPI_KEY"):
    url = f"https://api.scraperapi.com/?api_key={api_key}&url=https://www.instagram.com/{username}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("title").text
            return {"status": "success", "title": title}
        else:
            return {"status": "error", "code": response.status_code}
    except Exception as e:
        return {"status": "exception", "error": str(e)}

# Apify
def verificar_via_apify(username, apify_token="YOUR_APIFY_TOKEN"):
    actor_id = "apify/instagram-profile-scraper"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {apify_token}"}
    input_data = {"usernames": [username], "resultsLimit": 1}
    run_url = f"https://api.apify.com/v2/actor-tasks/{actor_id}/runs?token={apify_token}"
    run_response = requests.post(run_url, json=input_data, headers=headers)

    if run_response.status_code == 201:
        run_data = run_response.json()
        run_id = run_data["data"]["id"]
        time.sleep(10)
        result_url = f"https://api.apify.com/v2/actor-runs/{run_id}/dataset/items?token={apify_token}"
        result_response = requests.get(result_url)
        if result_response.ok:
            return {"status": "success", "data": result_response.json()}
        else:
            return {"status": "error", "msg": result_response.text}
    return {"status": "failed", "reason": run_response.text}

# Google Search (usando SerpAPI ou método de scraping)
def buscar_no_google(username):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = f"site:instagram.com inurl:{username}"
    url = f"https://www.google.com/search?q={query}"
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = [a.text for a in soup.find_all('h3')]
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# Fuzzy Matching
def verificar_com_fuzzy(username):
    base_names = ["caio.godoy", "caiogodoy_", "godoycaio123"]
    similar = []
    for name in base_names:
        ratio = SequenceMatcher(None, username.lower(), name.lower()).ratio()
        if ratio > 0.6:
            similar.append((name, round(ratio, 2)))
    return {"status": "success", "similar_users": similar}
