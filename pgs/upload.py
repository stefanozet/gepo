import pandas as pd
import streamlit as st

def upload(file_ext = ['csv', 'xls', 'txt'], input_separator = [';', '|', ','], rows_to_display = 10):
    
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type = file_ext, 
        accept_multiple_files=False, 
        help="Load an file csv, xls or drang & drop it on the form."
        )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        cf_rows_to_display = st.number_input(
            'Insert a number of rows to display', 
            min_value=1, max_value=100, value=rows_to_display, step=10, format='%i'
            )

    with col2:
        if uploaded_file and (
            uploaded_file.type == 'text/csv' \
            or uploaded_file.type == 'text/plain'):
            separator = st.selectbox(
                'Which is the separator?',
                input_separator
                )
    
    with col3:
        if uploaded_file:
            st.write("<div class='block_widget'>File type: {}</div>".format(uploaded_file.type), unsafe_allow_html=True)

    with col4:
        # st.button("Go to elaboration section", )
        ''

    if uploaded_file:
        if uploaded_file.type == 'text/csv'	\
            or uploaded_file.type == 'text/plain':
            dataframe = pd.read_csv(uploaded_file, sep=separator)
        else:
            dataframe = pd.read_excel(uploaded_file)

        st.dataframe(dataframe.head(cf_rows_to_display))
        st.session_state.df = dataframe
