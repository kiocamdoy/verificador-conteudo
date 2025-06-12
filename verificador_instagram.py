
import instaloader
import os
from dotenv import load_dotenv
from difflib import get_close_matches

# Carrega variáveis do .env
load_dotenv("login.env")

INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASS = os.getenv("INSTAGRAM_PASS")

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username

    username_clean = username[1:]
    loader = instaloader.Instaloader()

    try:
        loader.login(INSTAGRAM_USER, INSTAGRAM_PASS)
        profile = instaloader.Profile.from_username(loader.context, username_clean)
        verificado = "✅ Perfil verificado" if profile.is_verified else "❌ Perfil não verificado"
        seguidores = f"👥 Seguidores: {profile.followers}"
        bio = f"📝 Bio: {profile.biography if profile.biography else 'Nenhuma bio encontrada'}"

        # Base simulada de nomes de perfis
        base_nomes = [
            "nebraskarenovation", "nebraska.renovation", "renovationnebraska", "nebraskareno", "nebraskaconstruction"
        ]

        semelhantes = get_close_matches(username_clean.lower(), base_nomes, n=3, cutoff=0.6)
        similares_formatados = "\n".join(f"• @{s}" for s in semelhantes)
        alerta_similar = f"🔍 Perfis com nomes parecidos encontrados:\n{similares_formatados}" if semelhantes else "✅ Nenhum perfil semelhante suspeito encontrado."

        return f"📱 Perfil analisado: @{profile.username}\n\n{verificado}\n{seguidores}\n{bio}\n\n{alerta_similar}"

    except Exception as e:
        return f"❌ Não foi possível verificar o perfil {username}.\nErro: {str(e)}"
