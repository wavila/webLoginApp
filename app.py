import streamlit as st
from Pages import page_login, page_main
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

st.title("DEMO")

if 'PAGE_ATUAL' not in st.session_state:
    st.session_state['PAGE_ATUAL'] = "LOGIN"

PAGE_ATUAL = st.session_state['PAGE_ATUAL']

logger.info('page atual')
logger.info(PAGE_ATUAL)

if PAGE_ATUAL == "LOGIN":
    page_login.login_page()

if PAGE_ATUAL == "MAIN":
    page_main.main_page()
