import streamlit as st
from verificador_instagram_integrado import verificar_perfil_completo

st.set_page_config(page_title="🔎 Verificador de Conteúdo e Perfis", layout="wide")
st.title("🔎 Verificador de Conteúdo e Perfis")

tipo_verificacao = st.selectbox("O que você deseja verificar?", ["Perfil do Instagram"])

if tipo_verificacao == "Perfil do Instagram":
    username = st.text_input("Insira o @ do perfil:", placeholder="@exemplo")
    if st.button("Verificar Perfil") and username:
        with st.spinner("Verificando perfil..."):
            resultado = verificar_perfil_completo(username.strip("@"))
        st.markdown("### Resultado:")
        st.markdown(resultado)
