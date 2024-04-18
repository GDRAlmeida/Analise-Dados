import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('Dados_Diabetes.csv', sep=';')

# Criando o gráfico de pizza
st.title('Gráfico de Pizza para Diabetes')

# Verificando se a coluna 'diabetes' está presente
if 'diabetes' in df.columns:
    # Separando os dados de diabéticos com valores 0 e 1
    diabetes_0 = df[df['diabetes'] == 0]
    diabetes_1 = df[df['diabetes'] == 1]
    
    # Contando os valores únicos em cada série
    diabetes_counts_0 = diabetes_0.shape[0]
    diabetes_counts_1 = diabetes_1.shape[0]

    # Exibindo os contagens
    st.write("Contagem de Diabéticos (Diabetes = 0):", diabetes_counts_0)
    st.write("Contagem de Diabéticos (Diabetes = 1):", diabetes_counts_1)

    # Dados para plotagem
    labels = ['Diabetes = 0', 'Diabetes = 1']
    sizes = [diabetes_counts_0, diabetes_counts_1]

    # Cria um gráfico de pizza
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
 
    # Exibe o gráfico no Streamlit
    st.pyplot(plt)
else:
    st.error("A coluna 'Diabetes' não foi encontrada no DataFrame.")
