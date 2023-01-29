import pandas as pd
import streamlit as st

def drop():
    
	if 'df' in st.session_state:
		df = st.session_state.df

		df_col = []
		if st.button("Save and drop columns not selected."):
			st.balloons()
			st.session_state.df = df[df_col]

		df_col = st.multiselect("Select Column you want to keep: ", options=list(df.columns),default=list(df.columns))
		st.dataframe(df[df_col])
