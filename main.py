import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from st_on_hover_tabs import on_hover_tabs
from pages.pg_upload import upload
from pages.pg_edit import edit

#------------------------------------------------------------------------------#
# Parametri di configurazione                                                  #
#------------------------------------------------------------------------------#
input_separator = ';', '|', ','
file_ext = ['csv','xls']
rows_to_display = 10

#------------------------------------------------------------------------------#
# Inizializzazione e funzioni                                                  #
#------------------------------------------------------------------------------#
uploaded_file = None

st.set_page_config(layout="wide")
st.markdown('<style>' + open('./static/style.css').read() + '</style>', unsafe_allow_html=True)


#------------------------------------------------------------------------------#
# Pagina principale                                                            #
#------------------------------------------------------------------------------#
st.title("CSV Toools")

with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['Upload', 'Edit', 'Export'], 
        iconName=['upload', 'edit', 'download'], 
        default_choice=0
    )
    st.session_state.tabs = tabs

if tabs =='Upload':
    st.header('{}'.format(tabs))
    upload(file_ext, input_separator, rows_to_display)
    # if st.button("Go to edit!"): 
    #     tabs = 'Edit'
    #     st.write('ciao ciao')

elif tabs == 'Edit':
    st.header('{}'.format(tabs))
    edit()

elif tabs == 'Export':
    st.header('{}'.format(tabs))
    if 'df' in st.session_state:
        st.dataframe(st.session_state.df)
    else:
        st.write("What do you do?")
        st.write("Please, before all, load something in upload page.")


        # st.download_button(
        #     label="Download data as CSV",
        #     data=convert_df_to_csv(dataframe),
        #     file_name=file_output_name+'.csv',
        #     mime='text/csv',
        # )


            # file_output_name = st.text_input(
                # 'Which name for output file?',
                # value=file_output_name
                # )

    # st.image("https://static.streamlit.io/examples/owl.jpg", width=200)