import pandas as pd
import streamlit as st

# st.set_page_config(
#     layout="wide",
#     page_title="Ciaoo",
#     page_icon="👋",
# )

def edit(): # pd.DataFrame:

    if 'df' in st.session_state:
        df = st.session_state.df

        tab1, tab2, tab3 = st.tabs(["Info", "Drop", "Elaborate"])
    
        with tab1:
            ''
        with tab2:
            ''
        with tab3:
            ''
        st.dataframe(st.session_state.df)

    else:
        st.write("What do you do?")
        st.write("Please, before all, load something in upload page.")
