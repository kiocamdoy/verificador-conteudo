
import streamlit as st
from verificador_links import verificar_link

st.set_page_config(page_title="Verificador de Conteúdo e Perfis", layout="centered")

st.markdown("## 🔍 Verificador de Conteúdo e Perfis")
tipo_verificacao = st.selectbox("O que você deseja verificar?", ["Link de notícia", "Perfil do Instagram"])

entrada = st.text_input("Insira o link da notícia:" if tipo_verificacao == "Link de notícia" else "Insira o @ do perfil:")

if st.button("Verificar Link" if tipo_verificacao == "Link de notícia" else "Verificar Perfil"):
    if tipo_verificacao == "Link de notícia":
        resultado = verificar_link(entrada)
        st.markdown("### Resultado:")
        if resultado:
            st.markdown(f"🔗 **Link formatado:** [{resultado['link_formatado']}]({resultado['link_formatado']})")
            st.markdown(f"📶 **Status do site:** {resultado['status_code']}")
            st.markdown(f"🟢 **Acessível:** {'Sim' if resultado['acessivel'] else 'Não'}")
        else:
            st.error("❌ Link inválido ou inacessível.")
    else:
        st.warning("Verificação de perfil ainda não implementada nesta versão.")
