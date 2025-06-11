
def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username

    suspeitos = ["_oficial", "investidor", "trader", "ganhe", "bitcoin"]
    alerta = "⚠️ Nome de perfil contém termos frequentemente usados em golpes." if any(s in username.lower() for s in suspeitos) else "✅ Nenhum termo suspeito no nome."

    verificado = "❌ Perfil não verificado."  # Em uma versão futura, podemos puxar isso com scraping ou API privada

    return f"📱 Perfil analisado: {username}\n\n{verificado}\n{alerta}"
