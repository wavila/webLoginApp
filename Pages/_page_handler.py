import streamlit as st
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def changePage(PAGE):
    st.session_state['PAGE_ATUAL'] = PAGE
    logger.info('change page')
    logger.info(PAGE)
    st.experimental_rerun()
