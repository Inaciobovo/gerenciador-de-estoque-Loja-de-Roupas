
import streamlit as st 
import pandas as pd
import numpy as np
from utils.cadastrarProdutos import cadastroProduto

def menu():
    st.title("Bella Modas - Central de Vendas")
    st.write("Aqui está o grafico atualizado de entrada e saida!")

    
   
    aba = st.sidebar.radio(
        "Menu",
        ("Menu","Cadastro de Produtos", "Relatórios", "Estoque", "Criar Pedidos")
    )

    if aba == "Menu":
        # Exemplo de conteúdo no menu
        data = pd.DataFrame(
            np.random.randn(10, 5),
            columns=['coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5']
        )

        st.subheader("Exemplo de Gráfico")
        st.line_chart(data)
    elif aba == "Cadastro de Produtos":
        cadastroProduto()
    