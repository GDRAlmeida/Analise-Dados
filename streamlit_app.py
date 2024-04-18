import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o layout de grade
col1, _, col2 = st.columns([2, 0.5, 1])

# Exibindo a depuração na primeira coluna
with col1:
    st.title('Depuração')
    st.write(df)

# Adicionando um espaço entre as colunas
st.write('')

# Criando o gráfico na segunda coluna
with col2:
    st.title('Gráfico para Diabetes')

    # Verificando se a coluna 'diabetes' está presente
    if 'diabetes' in df.columns:
        # Contando os valores únicos na coluna 'Diabetes'
        diabetes_counts = df['diabetes'].value_counts()
        
        # Exibindo o gráfico de barras com tons de cinza
        plt.bar(diabetes_counts.index, diabetes_counts.values, color='gray')
        plt.xticks(np.arange(len(diabetes_counts)), ['Não Diabéticos', 'Diabéticos'])
        plt.xlabel('Diabetes')
        plt.ylabel('Contagem')
        plt.title('Contagem de Diabéticos')
        st.pyplot(plt)
        st.write(diabetes_counts)
    else:
        st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
