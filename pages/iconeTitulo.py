import datetime
import streamlit as st


st.set_page_config(layout="centered", page_title="A certain gacha calculator", page_icon="https://img.game8.co/3316382/66059bcd59dcf0666c66bf1b5902dc2b.png/show")



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

with st.sidebar:
     st.title("Titulo")
     st.write("Batata")