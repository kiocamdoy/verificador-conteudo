
import requests

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username
    user = username[1:]

    url = "https://instagram-profile1.p.rapidapi.com/getprofile"
    headers = {
        "X-RapidAPI-Key": "2b54a3f18fmshfcada5b2e80c279p12072ejsncc9e1d2a188c",
        "X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com"
    }
    params = { "username": user }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.status_code != 200:
            return f"❌ Não foi possível acessar o perfil @{user}. Código: {response.status_code}"

        data = response.json()
        profile = data.get("data", {})

        if not profile:
            return f"❌ Perfil @{user} não encontrado."

        verificado = "✅ Verificado" if profile.get("isVerified") else "❌ Não verificado"
        seguidores = profile.get("followerCount", 0)
        nome = profile.get("fullName", "Desconhecido")
        bio = profile.get("biography", "")

        return f"📱 {nome} (@{user})\n{verificado}\n👥 Seguidores: {seguidores}\n📝 Bio: {bio or 'Sem bio'}"

    except Exception as e:
        return f"❌ Erro ao consultar perfil @{user}: {str(e)}"
