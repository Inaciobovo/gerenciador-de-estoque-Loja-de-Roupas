import streamlit as st
import views.menu as menu

def loginPrincipal():
    USUARIO = "admin"
    SENHA = "admin123"
    #tela de login
    if "acesso_liberado" not in st.session_state:
        st.session_state["acesso_liberado"] = False
    if not st.session_state["acesso_liberado"]:

        with st.form("form_login", clear_on_submit=False):
            st.image("img/logo.png", width=400) 
            usuario_log = st.text_input("Usuário")
            senha_log = st.text_input("Senha", type="password")
            login_btn = st.form_submit_button("Login")

            if login_btn:
                if usuario_log == USUARIO and senha_log == SENHA:
                    st.success("Login realizado com sucesso!")
                    st.session_state["acesso_liberado"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos, tente novamente.")

    #pos login
    if st.session_state["acesso_liberado"]:
        if st.sidebar.button("Sair"):
            st.session_state["acesso_liberado"] = False
            st.rerun()

        menu.menu()