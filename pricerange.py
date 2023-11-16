import streamlit as st
import pandas as pd
import plotly.express as px

 
st.write("""Price comparision of the cars""")
 
df = pd.read_csv("pricerange.csv")
x=df['Car']
y=df['PriceRange(Lakhs)']
fig = px.bar(x=x, y=y, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='pricerange')
st.plotly_chart(fig)

