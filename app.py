import streamlit as st
from verificador_links import verificar_link
from verificador_instagram_integrado import verificar_perfil_completo

st.set_page_config(page_title="Verificador de Conteúdo e Perfis", page_icon="🔍")
st.title("🔍 Verificador de Conteúdo e Perfis")

opcao = st.selectbox("O que você deseja verificar?", ["Link de notícia", "Perfil do Instagram"])

if opcao == "Link de notícia":
    url = st.text_input("Insira o link da notícia:")
    if st.button("Verificar Link") and url:
        resultado = verificar_link(url)

        st.subheader("Resultado:")
        st.markdown(f"🔗 Link analisado: [{url}]({url})")

        if resultado['criado_em']:
            st.markdown(f"📅 Domínio criado em: {resultado['criado_em']}")

        if resultado['termos_suspeitos']:
            st.markdown("❌ Termos suspeitos encontrados:")
            for termo in resultado['termos_suspeitos']:
                st.markdown(f"- {termo}")
        else:
            st.markdown("✅ Nenhum termo suspeito encontrado.")

        if resultado['noticias_semelhantes']:
            st.markdown("📰 Notícias similares confiáveis:")
            for link in resultado['noticias_semelhantes']:
                st.markdown(f"• [{link}]({link})")

        if resultado['seguro']:
            st.markdown("🛡️ Segurança do site: ✅ URL limpa segundo o Google Safe Browsing.")
        else:
            st.markdown("🛑 Segurança do site: URL considerada maliciosa ou suspeita.")

elif opcao == "Perfil do Instagram":
    perfil = st.text_input("Insira o @ do perfil:")
    if st.button("Verificar Perfil") and perfil:
        resultado = verificar_perfil_completo(perfil)

        st.subheader("Resultado:")
        if resultado['erro']:
            st.error(f"❌ Não foi possível verificar o perfil @{perfil}. Erro: {resultado['erro']}")
        else:
            st.markdown(f"📱 Perfil analisado: @{perfil}")
            st.markdown(f"🔗 Link: [https://instagram.com/{perfil}](https://instagram.com/{perfil})")

            if resultado['verificado']:
                st.markdown("✅ Perfil verificado pelo Instagram")
            else:
                st.markdown("❌ Perfil não verificado.")

            if resultado['termos_suspeitos']:
                st.markdown("⚠️ Termos suspeitos encontrados no nome ou bio:")
                for termo in resultado['termos_suspeitos']:
                    st.markdown(f"- {termo}")
            else:
                st.markdown("✅ Nenhum termo suspeito no nome ou bio.")

            if resultado['similares']:
                st.markdown("🔍 Perfis com nomes semelhantes encontrados:")
                for nome in resultado['similares']:
                    st.markdown(f"• @{nome}")

            if resultado['descricao']:
                st.markdown(f"📝 Bio: {resultado['descricao']}")

            if resultado['seguidores']:
                st.markdown(f"👥 Seguidores: {resultado['seguidores']}")
            if resultado['seguindo']:
                st.markdown(f"➡️ Seguindo: {resultado['seguindo']}")
            if resultado['posts']:
                st.markdown(f"🖼️ Publicações: {resultado['posts']}")
