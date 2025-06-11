
import difflib

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username

    suspeitos = ["_oficial", "investidor", "trader", "ganhe", "bitcoin"]
    alerta_nome = "⚠️ Nome de perfil contém termos frequentemente usados em golpes." if any(s in username.lower() for s in suspeitos) else "✅ Nenhum termo suspeito no nome."

    # Simulação de perfil verificado (futuro: scraping ou API real)
    verificado = "❌ Perfil não verificado."

    # Simulação de perfis semelhantes (futuro: IA + scraping)
    similares = ["@caio.godoy", "@caiogodoy_", "@godoycaio123"]
    similares_formatados = "\n".join(f"• {s}" for s in similares)
    alerta_similar = f"🔍 Perfis com nomes semelhantes encontrados:\n{similares_formatados}"

    return f"📱 Perfil analisado: {username}\n\n{verificado}\n{alerta_nome}\n\n{alerta_similar}"
