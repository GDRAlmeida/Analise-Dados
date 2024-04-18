import streamlit as st
import pandas as pd
from Main import df

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Contando os valores únicos na coluna 'Diabetes'
diabetes_counts = df['diabetes'].value_counts()

# Exibindo o gráfico de pizza
st.write(diabetes_counts)
