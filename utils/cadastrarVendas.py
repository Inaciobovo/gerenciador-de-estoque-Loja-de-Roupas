import streamlit as st

def cadastrarVendas():
    st.title("Cadastro de Vendas")
    produto = st.text_input("Produto Vendido")
    quantidade = st.number_input("Quantidade Vendida", min_value=1, step=1)
    preco_unitario = st.number_input("Preço Unitário (R$)", min_value=0.0, format="%.2f")
    cadastrar_btn = st.button("Cadastrar Venda")
    

    if cadastrar_btn:
        total = quantidade * preco_unitario
        st.success(f"Venda cadastrada com sucesso! Total: R$ {total:.2f}")