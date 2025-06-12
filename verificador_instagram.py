
import requests

def verificar_perfil_instagram(username):
    if not username.startswith("@"):
        username = "@" + username
    user = username[1:]

    url = f"https://www.instagram.com/{user}/?__a=1&__d=dis"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return f"❌ Não foi possível acessar o perfil @{user}. Código: {response.status_code}"

        data = response.json()
        profile_data = data.get("graphql", {}).get("user", {})

        if not profile_data:
            return f"❌ Perfil @{user} não encontrado."

        verificado = "✅ Verificado" if profile_data.get("is_verified") else "❌ Não verificado"
        seguidores = profile_data.get("edge_followed_by", {}).get("count", 0)
        bio = profile_data.get("biography", "")

        return f"Perfil: @{user}\n{verificado}\nSeguidores: {seguidores}\nBio: {bio or 'Sem bio'}"

    except Exception as e:
        return f"❌ Erro ao consultar perfil @{user}: {str(e)}"
