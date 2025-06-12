
import instaloader
from difflib import get_close_matches

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username

    username_clean = username[1:]
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username_clean)
        verificado = "✅ Perfil verificado" if profile.is_verified else "❌ Perfil não verificado"
        seguidores = f"👥 Seguidores: {profile.followers}"
        bio = f"📝 Bio: {profile.biography if profile.biography else 'Nenhuma bio encontrada'}"

        # Simulação de base local de nomes de perfis comuns
        base_nomes = [
            "alinefonseca", "aline_fonseca", "aline.fon", "alinefonceca", "alinnefonseca",
            "alinf", "fonsecaa", "a_linf", "alinef", "aline_f"
        ]

        semelhantes = get_close_matches(username_clean.lower(), base_nomes, n=3, cutoff=0.6)
        similares_formatados = "\n".join(f"• @{s}" for s in semelhantes)
        alerta_similar = f"🔍 Perfis com nomes parecidos encontrados:\n{similares_formatados}" if semelhantes else "✅ Nenhum perfil semelhante suspeito encontrado."

        return f"📱 Perfil analisado: @{profile.username}\n\n{verificado}\n{seguidores}\n{bio}\n\n{alerta_similar}"

    except Exception as e:
        return f"❌ Não foi possível verificar o perfil {username}.\nErro: {str(e)}"
