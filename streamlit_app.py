import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Imprimindo o DataFrame para depuração
st.write(df)

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Verificando se a coluna 'diabetes' está presente
if 'diabetes' in df.columns:
    # Contando os valores únicos na coluna 'Diabetes'
    diabetes_counts = df['diabetes'].value_counts()
    
    # Exibindo o gráfico de pizza
    st.write(diabetes_counts)
else:
    st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")

fig, ax = plt.subplots()
ax.hist(diabetes_counts, bins=20)

st.pyplot(fig)
