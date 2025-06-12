
import requests
from urllib.parse import urlparse
import whois

SAFE_BROWSING_API_KEY = "AIzaSyATSZEXWFZcXoBEuFKMwBOuZambpWFf4kk"
SERPAPI_KEY = "507c5bd1-eecc-4af4-b309-cf744f42e102"

def verificar_seguranca_url_safebrowsing(url, api_key):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {
        "client": {
            "clientId": "verificador-links",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(f"{endpoint}?key={api_key}", json=payload)
    data = response.json()

    if "matches" in data:
        return "❌ CUIDADO! Esta URL foi sinalizada como perigosa pelo Google Safe Browsing."
    return "✅ Nenhuma ameaça detectada pelo Google Safe Browsing no momento.\n⚠️ Atenção: sites novos ou pouco conhecidos ainda podem representar riscos não identificados."

def buscar_noticias_relacionadas(url):
    query = url.split("/")[-1].replace("-", " ")[:100]
    params = {
        "engine": "google",
        "q": query,
        "tbm": "nws",
        "api_key": SERPAPI_KEY
    }
    response = requests.get("https://serpapi.com/search", params=params)
    noticias = response.json().get("news_results", [])
    if not noticias:
        return "Nenhuma notícia relacionada encontrada em fontes confiáveis."
    return "\n".join([f"• [{n['title']}]({n['link']})" for n in noticias[:3]])

def verificar_link(url):
    try:
        dominio = urlparse(url).netloc
        info = whois.whois(dominio)

        suspeito = any(x in url.lower() for x in ["politica", "urgente", "milagre", "ganhe dinheiro", "exclusivo"])
        reputacao = "Domínio criado em: " + str(info.creation_date)
        alerta = "⚠️ Conteúdo pode conter termos sensacionalistas." if suspeito else "✅ Nenhum termo suspeito encontrado."

        noticias_relacionadas = buscar_noticias_relacionadas(url)
        alerta_segurança = verificar_seguranca_url_safebrowsing(url, SAFE_BROWSING_API_KEY)

        return f"🔗 Link analisado: {url}\n\n{reputacao}\n{alerta}\n\n🗞️ Notícias confiáveis relacionadas:\n{noticias_relacionadas}\n\n🛡️ Segurança do site:\n{alerta_segurança}"

    except Exception as e:
        return f"❌ Erro ao verificar o link: {str(e)}"
