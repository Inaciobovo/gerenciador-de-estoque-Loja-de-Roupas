import streamlit as st
from utils.cadastrarVendas import cadastrarVendas


def iniciarRegistroDoDia():
    st.title("Iniciar Dia")
    st.write("Aqui você pode iniciar o dia de trabalho.")
    iniciar__btn = st.button("Iniciar Dia")

    if iniciar__btn:
        st.success("Dia iniciado com sucesso!")

    cadastrarVendas()

        

def finalizarDia():
    st.title("Finalizar Dia")
    st.write("Aqui você pode finalizar o dia de trabalho.")
    finalizar_btn = st.button("Finalizar Dia")

    if finalizar_btn:
        st.success("Dia finalizado com sucesso!")