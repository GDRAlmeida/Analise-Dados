import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Contando os valores únicos na coluna 'Diabetes'
diabetes_counts = df['Diabetes'].value_counts()

# Exibindo o gráfico de pizza
st.write(diabetes_counts)
