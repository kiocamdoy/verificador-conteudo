
import requests
from urllib.parse import urlparse
import datetime

def verificar_link_completo(link):
    if not link.startswith("http://") and not link.startswith("https://"):
        link = "https://" + link

    resultado = ""
    try:
        # 1. Verificar se o link é válido e acessível
        response = requests.get(link, timeout=5)
        status_code = response.status_code

        if status_code != 200:
            return f"❌ Link inacessível. Código de status: {status_code}"

        # 2. Verificar a data de criação do domínio (via WhoisXMLAPI, por exemplo)
        domain = urlparse(link).netloc
        whois_url = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
        headers = {'X-Api-Key': 'SUA_CHAVE_API_AQUI'}
        whois_response = requests.get(whois_url, headers=headers)
        if whois_response.status_code == 200:
            whois_data = whois_response.json()
            creation_date = whois_data.get("creation_date")
            if creation_date:
                resultado += f"🗓️ Domínio criado em: {creation_date}"
        else:
            resultado += "⚠️ Não foi possível verificar a data de criação do domínio."

        # 3. Verificar se contém termos suspeitos
        termos_suspeitos = ["boato", "mentira", "farsa", "enganoso"]
        if any(palavra in link.lower() for palavra in termos_suspeitos):
            resultado += " ⚠️ Termo potencialmente suspeito no link."

        # 4. Verificação contra mecanismos de segurança (Google Safe Browsing ou VirusTotal)
        resultado += "\n✅ Link analisado: " + link

    except Exception as e:
        resultado = f"❌ Erro ao processar o link: {str(e)}"

    return resultado
