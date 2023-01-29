import pandas as pd
import streamlit as st

def drop():
    
	if 'df' in st.session_state:
		df = st.session_state.df

		if 'df_col' not in locals(): df_col = []
		if st.button("Save and drop columns not selected."):
			st.balloons()
			df = df[df_col]
			st.session_state.df = df
			# df = df.drop(columns=['RIFERIMENTO', 'CLIENTE.NAZ'])
			
		df_col = st.multiselect("Select Column you want to keep: ", options=list(df.columns),default=list(df.columns))
		st.dataframe(df[df_col])
