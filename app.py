import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análise de Dados")

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

hist_button = st.button('Criar histograma') # botão para criar histograma
scatter_button = st.button('Criar gráfico de dispersão') # botão para criar gráfico de dispersão

if hist_button: # Se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(
        car_data, 
        x="odometer"
    ) # criar um histograma

    st.plotly_chart(fig, width="stretch") # exibindo o histograma

if scatter_button: # Se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )
    st.plotly_chart(fig, width="stretch")