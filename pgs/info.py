import streamlit as st
import pandas as pd



def info():

    if 'df' in st.session_state:
        df = st.session_state.df
        df_col =st.multiselect("Select Column: by default first 10", options=list(df.columns),default=list(df.columns[0:9]))
        st.subheader("Show DataFrame") 
        last_page = len(df)
        N_df = 10
        if not "page_number_df" in st.session_state:
            st.session_state["page_number_df"] = 0
        prev,next,first,last = st.columns([1,2,1,18])
        if next.button("Next", type="primary", key='sf_button_next'):
          if st.session_state["page_number_df"] + 1 > last_page:
              st.session_state["page_number_df"] = 0
          else:
              st.session_state["page_number_df"] += 1
        if prev.button("Prev",type="primary",key='sf_button_prev'):
          if st.session_state["page_number_df"] - 1 < 0:
              st.session_state["page_number_df"] = last_page
          else:
              st.session_state["page_number_df"] -= 1
        ti_start_idx = st.session_state["page_number_df"] * N_df
        ti_end_idx = (1 + st.session_state["page_number_df"]) * N_df
        if (ti_start_idx > last_page) | (ti_end_idx < 0) | (ti_end_idx > last_page):
            ti_start_idx , ti_end_idx = 0,N_df
            st.session_state["page_number_df"] = 0
        if first.button("First",type="primary",key='first'):
            st.session_state["page_number_df"] = 0
            ti_start_idx=st.session_state["page_number_df"]
            ti_end_idx = st.session_state["page_number_df"] +N_df   
        if last.button("Last",type="primary",key='last'):
            st.session_state["page_number_df"] = (last_page//N_df) -1
            ti_start_idx=last_page -N_df
            ti_end_idx = last_page  
        sub_df = df.iloc[ti_start_idx:ti_end_idx]
        st.dataframe(sub_df[df_col])
        st.dataframe(df[df_col])
        st.write("Page",st.session_state["page_number_df"]+1, "of",max(last_page//N_df, st.session_state['page_number_df']))
