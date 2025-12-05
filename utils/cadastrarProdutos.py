import streamlit as st
def cadastroProduto():
    st.title("Cadastro de Produtos")
    descricao = st.text_input("Descrição do Produto")
    codigo = st.text_input("Código do Produto")
    preco = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade em Estoque", min_value=0, step=1)
    cadastrar_btn = st.button("Cadastrar Produto")

    if cadastrar_btn:
        st.success(f"Produto '{descricao}' cadastrado com sucesso!")