import streamlit as st

fileupload_pg = st.Page("fileupload.py", title="File Upload", icon=":material/upload:")
event_status_pg = st.Page("event_status.py", title="event_status", icon=":material/update:")
pg = st.navigation([fileupload_pg, event_status_pg ])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
