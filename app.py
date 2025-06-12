import streamlit as st
from verificador_instagram_integrado import verificar_perfil_completo

st.set_page_config(page_title="🔎 Verificador de Conteúdo e Perfis", layout="centered")

st.markdown("# 🔎 Verificador de Conteúdo e Perfis")
opcao = st.selectbox("O que você deseja verificar?", ["Perfil do Instagram"])

if opcao == "Perfil do Instagram":
    username = st.text_input("Insira o @ do perfil:", placeholder="@exemplo")
    if st.button("Verificar Perfil"):
        if username:
            resultado = verificar_perfil_completo(username)
            st.markdown("### Resultado:")
            st.write(resultado)
        else:
            st.warning("Por favor, insira um nome de usuário válido.")