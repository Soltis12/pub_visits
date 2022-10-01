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

## Connect to Snowflake
#
