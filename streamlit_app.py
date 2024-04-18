import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Contando os valores únicos na coluna 'Diabetes'
diabetes_counts = df['Diabetes'].value_counts()

# Exibindo o gráfico de pizza
fig, ax = plt.subplots()
ax.pie(diabetes_counts, labels=diabetes_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
