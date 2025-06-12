import streamlit as st
from verificador_instagram_integrado import verificar_perfil_completo
from verificador_links import verificar_link

st.set_page_config(page_title="Verificador de Conteúdo e Perfis", layout="centered")

st.markdown("## 🔍 Verificador de Conteúdo e Perfis")

opcao = st.selectbox("O que você deseja verificar?", ["Perfil do Instagram", "Link de notícia"])

entrada = ""
if opcao == "Perfil do Instagram":
    entrada = st.text_input("Insira o @ do perfil:", placeholder="@exemplo")
    if st.button("Verificar Perfil") and entrada:
        resultado = verificar_perfil_completo(entrada)
        st.markdown("### Resultado:")
        st.write(resultado)

elif opcao == "Link de notícia":
    entrada = st.text_input("Insira o link da notícia:", placeholder="https://exemplo.com/noticia")
    if st.button("Verificar Link") and entrada:
        resultado = verificar_link(entrada)
        st.markdown("### Resultado:")
        st.markdown(resultado, unsafe_allow_html=True)