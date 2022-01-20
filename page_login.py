import streamlit as st
import logging
from Pages._page_handler import changePage
from postgres import Postgres
import os
db = Postgres(os.environ['DATABASE_URL'])

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def logar(login,password):
    user = db.one(f"SELECT * FROM login WHERE usr='{login}' and pas='{password}'")
    try:
        if user.usr == login:
            logger.info('login')
            changePage("UPLOAD PAGE")
        else:    
            logger.info('not login')
    except:
        t = st.empty()
        t.text('usuário e senha inválidos!')

def login_page():

    st.subheader("Login")

    login = st.text_input('login','')
    password = st.text_input('password','',type="password")
    
    if st.button('logar'):
        logar(login,password)