import pandas as pd
import streamlit as st

@st.cache
def convert_df(df: pd.DataFrame)-> None or str:
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def download():
    
	if 'df' in st.session_state:
		df = st.session_state.df

		csv = convert_df(df)

		st.download_button(
			label="Download data as CSV",
			data=csv,
			file_name='df.csv',
			mime='text/csv',
		)	
		st.dataframe(df)
        
	else:
		st.write("What do you do?")
		st.write("Please, before all, load something in upload page.")







