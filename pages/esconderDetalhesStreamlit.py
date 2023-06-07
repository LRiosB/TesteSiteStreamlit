import datetime
import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.expander('Sobre a aplicação'):
     st.write('Esta aplicação demonstra diversas maneiras de como você pode definir o layout da sua aplicação Streamlit')
     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
     d = st.date_input(
     "When\'s your birthday",
     datetime.date(2019, 7, 6))
     st.write('Your birthday is:', d)
