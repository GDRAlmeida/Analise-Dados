import streamlit as st
import pandas as pd
import plotly.express as px

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

    # Criando o gráfico de pizza com as informações de contagem usando Plotly
    fig = px.pie(values=diabetes_counts, names=diabetes_counts.index, 
                 title='Distribuição de Diabetes', labels=diabetes_counts.index)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
