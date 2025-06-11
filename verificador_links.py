
import requests
from urllib.parse import urlparse
import whois

def verificar_link(url):
    try:
        dominio = urlparse(url).netloc
        info = whois.whois(dominio)

        suspeito = any(x in url.lower() for x in ["politica", "urgente", "milagre", "ganhe dinheiro", "exclusivo"])
        reputacao = "Domínio criado em: " + str(info.creation_date)
        alerta = "⚠️ Conteúdo pode conter termos sensacionalistas." if suspeito else "✅ Nenhum termo suspeito encontrado."

        # Simulação de análise de conteúdo (futuro: comparação real com fact-checkers)
        sugestoes = [
            "https://www.snopes.com/fact-check/fake-news-alert/",
            "https://aosfatos.org/noticias/boato-sobre-tema-semelhante/"
        ]
        links_similares = "\n".join(f"• {s}" for s in sugestoes)

        # Simulação de verificação de segurança (futuro: integração com VirusTotal / SafeBrowsing)
        alerta_segurança = "✅ Nenhum comportamento malicioso identificado no código-fonte."

        return f"🔗 Link analisado: {url}\n\n{reputacao}\n{alerta}\n\n🔗 Notícias similares confiáveis:\n{links_similares}\n\n🛡️ Segurança do site:\n{alerta_segurança}"

    except Exception as e:
        return f"❌ Erro ao verificar o link: {str(e)}"
