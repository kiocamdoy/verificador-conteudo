import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

def verificar_perfil_completo(username):
    resultados = []

    # ScraperAPI
    try:
        r = requests.get(f"https://instagram.com/{username}", timeout=10)
        if r.status_code == 200 and username.lower() in r.text.lower():
            resultados.append("✔️ Página do Instagram acessível.")
        else:
            resultados.append("❌ Página do Instagram inacessível.")
    except Exception as e:
        resultados.append(f"❌ Erro no acesso ao perfil: {e}")

    # Fuzzy Matching (exemplo)
    similares = []
    for nome in ["caio.godoy", "caiogodoy_", "godoycaio123"]:
        score = fuzz.ratio(username.lower(), nome.lower())
        if score > 70:
            similares.append((nome, score))

    if similares:
        resultados.append("🔍 Perfis semelhantes encontrados:")
        for s in similares:
            resultados.append(f"- @{s[0]} (semelhança: {s[1]}%)")
    else:
        resultados.append("✅ Nenhum perfil semelhante encontrado.")

    return "\n".join(resultados)