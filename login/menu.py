# Arquivo: login/menu.py

# A importação do Streamlit é necessária dentro deste arquivo também!
import streamlit as st 

def menu():
    # 💥 Ponto de Verificação 1: Adicione um título muito claro
    
    st.title("PÁGINA PRINCIPAL DO SISTEMA")
    st.markdown("---")
    
    
    if st.button("Sair / Logout", type="primary"):
        st.session_state['acesso_liberado'] = False
        st.rerun()

    