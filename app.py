import streamlit as st
from verificador_instagram_integrado import verificar_perfil_completo
from verificador_links import verificar_link_noticia

st.set_page_config(page_title="Verificador de Conteúdo e Perfis")

st.title("🔍 Verificador de Conteúdo e Perfis")

opcao = st.selectbox("O que você deseja verificar?", ["Perfil do Instagram", "Link de Notícia"])

if opcao == "Perfil do Instagram":
    usuario = st.text_input("Insira o @ do perfil:", placeholder="@exemplo")
    if st.button("Verificar Perfil"):
        if usuario:
            resultado = verificar_perfil_completo(usuario.strip("@"))
            st.markdown(resultado)
        else:
            st.warning("Por favor, insira um nome de usuário.")

elif opcao == "Link de Notícia":
    url = st.text_input("Insira o link da notícia:")
    if st.button("Verificar Link"):
        if url:
            resultado = verificar_link_noticia(url)
            st.markdown(resultado)
        else:
            st.warning("Por favor, insira o link da notícia.")
