## Import packages
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

## Opening text
streamlit.title("🍺 Holly's Pub Visits 🍹")
streamlit.header("Visualizing Happiness in 2022")
streamlit.text("This tool is built to demonstrate usage of Snowflake, Python and APIs to import, clean, append to and visualize data")

# Function to display the table
def get_snowflake_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM PUBS_VISITED")
        return my_cur.fetchall()

## Load the data from Snowflake as a Pandas DataFrame
if streamlit.button('Display Pub Visits'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_snowflake_data()
    my_cnx.close
    streamlit.dataframe(my_data_rows)
