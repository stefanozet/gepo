import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from st_on_hover_tabs import on_hover_tabs
from pgs.pg_edit import edit
from pgs.pg_upload import upload

#------------------------------------------------------------------------------#
# Parametri di configurazione                                                  #
#------------------------------------------------------------------------------#
input_separator = ';', '|', ','
file_ext = ['csv','xls', 'txt']
rows_to_display = 10

#------------------------------------------------------------------------------#
# Inizializzazione e funzioni                                                  #
#------------------------------------------------------------------------------#
st.set_page_config(layout="wide")
st.markdown('<style>' + open('./static/style.css').read() + '</style>', unsafe_allow_html=True)

st.title("CSV Toools")

with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Upload', 'Edit', 'Export'], 
        iconName=['upload', 'edit', 'download'], 
        default_choice=0
    )
    st.session_state.tabs = tabs

# Pagina Upload
if tabs =='Upload':
    st.header('{}'.format(tabs))
    upload(file_ext, input_separator, rows_to_display)
    # if st.button("Go to edit!"): 
    #     tabs = 'Edit'
    #     st.write('ciao ciao')

#Pagina Edit
elif tabs == 'Edit':
    st.header('{}'.format(tabs))
    edit()

#Pagina Export
elif tabs == 'Export':
    st.header('{}'.format(tabs))
    if 'df' in st.session_state:
        st.dataframe(st.session_state.df)
    else:
        st.write("What do you do?")
        st.write("Please, before all, load something in upload page.")
