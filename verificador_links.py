
import requests
from urllib.parse import urlparse
import whois

def verificar_link(url):
    try:
        dominio = urlparse(url).netloc
        info = whois.whois(dominio)

        suspeito = any(x in url.lower() for x in ["politica", "urgente", "milagre", "ganhe dinheiro", "exclusivo"])
        reputacao = "Domínio criado em: " + str(info.creation_date)

        alerta = "⚠️ Conteúdo com termos sensacionalistas." if suspeito else "✅ Nenhum termo suspeito encontrado."

        return f"🔗 Link analisado: {url}\n\n{reputacao}\n{alerta}"

    except Exception as e:
        return f"❌ Erro ao verificar o link: {str(e)}"
