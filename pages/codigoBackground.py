import streamlit as st

st.set_page_config(page_title="Codigo background", page_icon="")

st.markdown("""
    <style>
        .stApp {
        background: url("https://preview.redd.it/hr5xh0zb46t51.png?width=640&crop=smart&auto=webp&s=96f0a1cfe9384358bafab44cb4723232b778add2");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)



st.header('st.checkbox')

st.write ('O que você gostaria de pedir?')

icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')

if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")

if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤")