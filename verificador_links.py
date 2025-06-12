import requests
from bs4 import BeautifulSoup
import difflib

fontes_confiaveis = [
    "bbc.com", "cnn.com", "nytimes.com", "reuters.com", "g1.globo.com",
    "uol.com.br", "folha.uol.com.br", "estadao.com.br", "theguardian.com"
]

def verificar_link_noticia(url):
    try:
        dominio = url.split("//")[-1].split("/")[0].replace("www.", "")
        similares = difflib.get_close_matches(dominio, fontes_confiaveis, n=1, cutoff=0.6)
        confiavel = dominio in fontes_confiaveis or bool(similares)
        status = "✅ Fonte confiável." if confiavel else "⚠️ Fonte possivelmente não confiável."

        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"❌ Não foi possível acessar a página (código {response.status_code})."

        soup = BeautifulSoup(response.content, "html.parser")
        titulo = soup.title.string.strip() if soup.title else "Sem título detectado"

        return f"{status}\n\n📰 **Título:** {titulo}"
    except Exception as e:
        return f"❌ Erro ao processar o link: {str(e)}"
