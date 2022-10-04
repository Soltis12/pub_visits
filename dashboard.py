## IMPORT PACKAGES
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


## WELCOME TEXT
streamlit.title("🍺 Holly's Pub Visits 🍹")
streamlit.header("Visualizing Happiness in 2022")
streamlit.text("This tool is built to demonstrate usage of Snowflake, Python and APIs")
streamlit.text("to import, clean, append to and visualize data")


## GLOBAL VARIABLES
# Headers for the PUBS_VISITED Snowflake table
v_snowflake_columns = ['Pub Name', 'City', 'Visit Date', 'Latitude', 'Longitude', 'Post Code', 'Post Code Area']
v_snowflake_entry_pub = 0
v_snowflake_entry_city = 0
v_snowflake_entry_date = 0

## DEFINE FUNCTIONS
# Function to display the table
def get_snowflake_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM PUBS_VISITED")
        return my_cur.fetchall()

# Function to add new pubs to the dataset
def add_pub(pub_name, city_name, date):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO PUBS_VISITED VALUES ('"+pub_name+"', '"+city_name+"', '"+date+"', NULL, NULL, NULL, NULL, NULL)")
        return ("Thank you for adding your visit to" + pub_name + ", " + city_name + " on " + date + " to the pub visit list")

# Function to search for a pub
def get_snowflake_data_pub(pub_name):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM PUBS_VISITED WHERE PUB_NAME = '"+pub_name+"'")
        return my_cur.fetchall()
                

## USER INTERACTIVE FEATURES
# Load the data from Snowflake as a Pandas DataFrame
if streamlit.button('Display Pub Visits'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_snowflake_data()
    my_cnx.close
    streamlit.dataframe(my_data_rows)

# Return data about a specific pub from Snowflake, if entered
try:
  pub_entry = streamlit.text_input("What pub would you ike information about",'The Imperial')
  if not pub_entry:
    streamlit.error("Please enter a pub name to get information")
  else:
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_snowflake_data_pub(pub_entry)
    my_cnx.close
    streamlit.dataframe(my_data_rows)
except URLError as e:
  streamlit.error()

# Add a pub visit to the Snowflake table 1: Pub Name
try:
  pub_entry = streamlit.text_input("What's the name of the pub?")
  if not pub_entry:
    streamlit.error("Please enter a pub name to continue")
  else:
    try:
      city_entry = streamlit.text_input("Which town or city is it in / nearest to?")
      if not city_entry:
        streamlit.error("Please enter a city name to continue")
      else:
        try:
          date_entry = streamlit.date_input("When was your visit?")
        except URLError as e:
          streamlit.error()        
    except URLError as e:
      streamlit.error()
except URLError as e:
  streamlit.error()
