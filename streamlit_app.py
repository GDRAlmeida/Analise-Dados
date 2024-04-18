import streamlit as st
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Verificando se a coluna 'diabetes' está presente
if 'diabetes' in df.columns:
    # Contando os valores únicos na coluna 'diabetes'
    diabetes_counts = df['diabetes'].value_counts()
    
    # Exibindo o gráfico de pizza
    st.write(diabetes_counts)

    # Criando o gráfico de pizza com as informações de contagem
    st.write("### Distribuição de Diabetes")
    st.plotly_chart(diabetes_counts.plot.pie(autopct='%1.1f%%', figsize=(8, 8)))
else:
    st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
