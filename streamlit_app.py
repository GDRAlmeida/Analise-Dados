import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o layout de grade
col1, _, col2 = st.columns([2, 0.1, 1])

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
        st.bar_chart(diabetes_counts, use_container_width=True)
        st.write(diabetes_counts)
    else:
        st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
