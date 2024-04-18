import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')
df['diabetes'] = df['diabetes'].replace({0: 'Não possui diabetes', 1: 'Possui diabetes'})

# Criando o layout de grade
col1, col2, col3 = st.columns([2,1,2])

# Exibindo a depuração na primeira coluna
with col1:
    st.title('Depuração')
    st.write(df)
    
with col2:
    st.write('')

# Criando o gráfico na segunda coluna
with col3:
    st.title('Gráfico para Diabetes')

    # Verificando se a coluna 'diabetes' está presente
    if 'diabetes' in df.columns:
        # Contando os valores únicos na coluna 'Diabetes'
        diabetes_counts = df['diabetes'].value_counts()
        
        # Exibindo o gráfico
        st.bar_chart(diabetes_counts, labels=x='Falso', 'Verdadeiro')
    else:
        st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
