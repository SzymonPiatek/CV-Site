import streamlit as st

st.set_page_config(page_title = 'My site', page_icon = ':blush:')

st.title('Projects')

st.write('You have entered', st.session_state['my_input'])