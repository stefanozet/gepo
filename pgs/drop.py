import pandas as pd
import streamlit as st

def drop():
    
	if 'df' in st.session_state:
		df = st.session_state.df

		if 'df_col' in st.session_state	and st.session_state.df_col != []:
			disable=False
		else:
			disable=True

		if st.button("Save and drop columns not selected.", disabled=disable):			
			df = df[st.session_state.df_col]
			st.session_state.df = df

		df_col = st.multiselect("Select Column you want to keep: ", options=list(df.columns),default=list(df.columns))
		st.session_state.df_col = df_col
		st.dataframe(df[df_col])
