import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button('Criar gráfico de dispersão') # criar um botão

st.header('Visualização interativa de dados sobre veículos')

if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

# criar uma caixa de seleção
#build_histogram = st.checkbox('Criar um histograma')

#if build_histogram: # se a caixa de seleção for selecionada
#    st.write('Criando um histograma para a coluna odometer')
