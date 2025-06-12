import requests
from bs4 import BeautifulSoup
import difflib
import json

def verificar_perfil_completo(username):
    resultados = []
    try:
        url = f"https://www.instagram.com/{username}/"
        headers = {
            "User-Agent": "Mozilla/5.0",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            scripts = soup.find_all("script", type="application/ld+json")
            if scripts:
                dados_json = json.loads(scripts[0].string.strip())
                nome = dados_json.get("name", "")
                descricao = dados_json.get("description", "")
                resultados.append(f"✅ Perfil encontrado: **{nome}**\n")
                resultados.append(f"📄 Bio: _{descricao}_\n")
            else:
                resultados.append("⚠️ Perfil encontrado, mas sem metadados detectáveis.")
        elif response.status_code == 404:
            resultados.append("❌ Perfil não encontrado.")
        else:
            resultados.append(f"⚠️ Erro ao acessar perfil (status {response.status_code})")
    except Exception as e:
        resultados.append(f"Erro: {str(e)}")
    return "\n".join(resultados)
