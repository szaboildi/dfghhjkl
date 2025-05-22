import os
os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"  # Disables problematic inspection

import streamlit as st
from utils import chat, llm_setup

model = llm_setup()

# App functionality
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Your query goes here"

query = st.text_input(
    "Please put your query below",
    label_visibility=st.session_state.visibility,
    disabled=st.session_state.disabled,
    placeholder=st.session_state.placeholder)


if query:
    st.write("Fetching your query...")
    st.write(chat(model, query))
