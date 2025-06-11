
import requests
from urllib.parse import urlparse
import whois

SAFE_BROWSING_API_KEY = "AIzaSyATSZEXWFZcXoBEuFKMwBOuZambpWFf4kk"

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

def verificar_link(url):
    try:
        dominio = urlparse(url).netloc
        info = whois.whois(dominio)

        suspeito = any(x in url.lower() for x in ["politica", "urgente", "milagre", "ganhe dinheiro", "exclusivo"])
        reputacao = "Domínio criado em: " + str(info.creation_date)
        alerta = "⚠️ Conteúdo pode conter termos sensacionalistas." if suspeito else "✅ Nenhum termo suspeito encontrado."

        sugestoes = [
            "https://www.snopes.com/fact-check/fake-news-alert/",
            "https://aosfatos.org/noticias/boato-sobre-tema-semelhante/"
        ]
        links_similares = "\n".join(f"• {s}" for s in sugestoes)

        alerta_segurança = verificar_seguranca_url_safebrowsing(url, SAFE_BROWSING_API_KEY)

        return f"🔗 Link analisado: {url}\n\n{reputacao}\n{alerta}\n\n🔗 Notícias similares confiáveis:\n{links_similares}\n\n🛡️ Segurança do site:\n{alerta_segurança}"

    except Exception as e:
        return f"❌ Erro ao verificar o link: {str(e)}"
