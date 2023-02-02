import pandas as pd
import streamlit as st
from pgs.info import info
from pgs.drop import drop

def edit(): # pd.DataFrame:

	if 'df' in st.session_state:
		#df = st.session_state.df

		tab1, tab2, tab3 = st.tabs(["Info", "Drop", "Elaborate"])

		with tab1:
			df = st.session_state.df
			info() #st.dataframe(st.session_state.df)
				
		with tab2:
			drop()
				
		with tab3:
			''

	else:
		st.write("What do you do?")
		st.write("Please, before all, load something in upload page.")