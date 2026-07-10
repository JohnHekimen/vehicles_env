import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análise de Dados para anúncios de vendas de carros")

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

hist_button = st.checkbox('Criar histograma') # botão para criar histograma

grafico = st.selectbox(
     'Escolha o gráfico que deseja visualizar', 
    ['Histograma', 'Gráfico de dispersão', 'Gráfico de barras']
) # menu suspenso para escolher o gráfico

if grafico == 'Histograma':
    fig = px.histogram(car_data, x="odometer")

else:
    fig = px.scatter(car_data, x="odometer", y="price")

st.plotly_chart(fig, width="stretch") # exibindo o gráfico