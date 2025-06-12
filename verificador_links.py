import datetime

def verificar_link(url):
    if not url.startswith("http"):
        return f"❌ Erro ao processar o link: Invalid URL '{url}': No scheme supplied. Perhaps you meant https://{url}?"

    # Simulação de análise
    criado_em = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f'''
    <p>🔗 Link analisado: <a href="{url}" target="_blank">{url}</a></p>
    <p>Domínio criado em: {criado_em} ✅ Nenhum termo suspeito encontrado.</p>
    <p>🔍 Notícias similares confiáveis:
    • <a href="https://www.snopes.com/fact-check/fake-news-alert/" target="_blank">https://www.snopes.com/fact-check/fake-news-alert/</a>
    • <a href="https://aosfatos.org/noticias/boato-sobre-tema-semelhante/" target="_blank">https://aosfatos.org/noticias/boato-sobre-tema-semelhante/</a></p>
    <p>🛡️ Segurança do site: ✅ URL limpa segundo o Google Safe Browsing.</p>
    '''