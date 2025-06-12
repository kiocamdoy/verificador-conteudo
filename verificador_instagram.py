
import instaloader

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username

    username = username[1:]  # remove o @ para o Instaloader funcionar
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        verificado = "✅ Perfil verificado" if profile.is_verified else "❌ Perfil não verificado"
        seguidores = f"👥 Seguidores: {profile.followers}"
        bio = f"📝 Bio: {profile.biography if profile.biography else 'Nenhuma bio encontrada'}"

        return f"📱 Perfil analisado: @{profile.username}\n\n{verificado}\n{seguidores}\n{bio}"
    except Exception as e:
        return f"❌ Não foi possível verificar o perfil @{username}.\nErro: {str(e)}"
