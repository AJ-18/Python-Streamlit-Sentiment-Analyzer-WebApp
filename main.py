import streamlit as st
import plotly.express as px
import pandas as pd
from backend import diary_sentiment

day = 21
entries = 0

st.title("Dairy Tone")

# Get the sentiment data
sentiment_list, pos_list, neg_list, dates = diary_sentiment(day, entries)

st.subheader("Positivity")

# Plot the positivity data
figure = px.line(x=dates, y=pos_list, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")

# Plot the negativity data
figure = px.line(x=dates, y=neg_list, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)