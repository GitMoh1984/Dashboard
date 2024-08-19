import pandas as pd
import streamlit as st
import cx_Oracle
import pandas
import os
from dotenv import load_dotenv
load_dotenv()
# Now you can access your environment variables using os.getenv
username = os.getenv('FODSUSER')
secret_key = os.getenv('FODSPASS')
database = os.getenv('FODSDBO')
st.title("welcome to DMT Dashboard")
on = st.toggle("Activate feature")
st.sidebar.markdown("# 🎈🎈🎈EVENT STATUS PENDING  🎈🎈🎈")
conn = cx_Oracle.connect(user=username, password=secret_key, dsn='FODSDEV', encoding="UTF-8")
cur = conn.cursor()
SelsqlTxt = """select PLAN_DET, EVENT_NM, EVENT_RUN_DT ,
EVENT_STATUS_CD,EVENT_CRT_DT FROM 
DMT_O.DMT_PLAN_EVENT_CNTL 
where EVENT_STATUS_CD  in ('PE','PR') 
order by 1 desc"""
print(SelsqlTxt)
results = cur.execute(SelsqlTxt)
sqldf = pd.read_sql(SelsqlTxt, conn)
columns = sqldf.columns.tolist()

st.write(sqldf.head(8))
selected_column = st.selectbox("Select Columns to Filter ", columns)
unique_values = sqldf[selected_column].unique()
selected_value = st.selectbox("Select Values to be Filtered", unique_values)
filtered_sqldf = sqldf[sqldf[selected_column] == selected_value]
st.write(filtered_sqldf)
st.button("Reset", type="primary")
if st.button("Update Event to CO"):
    Updsqltxt = f"""UPDATE DMT_O.DMT_PLAN_EVENT_CNTL SET EVENT_STATUS_CD = 'CO' where {selected_column} in '{selected_value}' """
    st.write(Updsqltxt)
    updresult= cur.execute(Updsqltxt)
    conn.commit()
    st.write(f"{selected_column} is update to Complete ")
else:
    st.write("Event Already updated thanks !!!")
cur.close()
conn.close()
