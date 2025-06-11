
import streamlit as st
from verificador_links import verificar_link
from verificador_instagram import verificar_perfil_instagram

st.title("🔍 Verificador de Conteúdo e Perfis")

opcao = st.selectbox("O que você deseja verificar?", ["Link de notícia", "Perfil do Instagram"])

if opcao == "Link de notícia":
    url = st.text_input("Insira o link da notícia:")
    if st.button("Verificar Link"):
        if url:
            resultado = verificar_link(url)
            st.write("### Resultado:")
            st.markdown(resultado)
        else:
            st.warning("Por favor, insira um link válido.")

elif opcao == "Perfil do Instagram":
    perfil = st.text_input("Insira o @ do perfil:")
    if st.button("Verificar Perfil"):
        if perfil:
            resultado = verificar_perfil_instagram(perfil)
            st.write("### Resultado:")
            st.markdown(resultado)
        else:
            st.warning("Por favor, insira um perfil válido.")
