import streamlit as st
import pandas as pd
import plotly.express as px
ch = {
    'chart': ['bar', 'line', 'scatter','box','histogram','pie'],
}

ch = pd.DataFrame(ch)


# Dropdown for selecting car type



st.title("EV camparisions")
df = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")
user_input_text_1 = st.text_input("parameter 1", key="text_input_1", value="")
user_input_text_2 = st.text_input("parameter 2", key="text_input_2", value="")
selected_chart = st.selectbox("Select Chart Type", ch['chart'].unique())


if st.button("Generate chart"):
   

    x=df[user_input_text_1]
    y=df[user_input_text_2]
    # Create chart based on the selected type
    if selected_chart == 'histogram':
        fig = px.histogram(df, x=user_input_text_1, labels={'x': 'X-axis'}, title='Histogram comparision')
    else:    
        if selected_chart == 'bar':
            fig = px.bar(df, x=user_input_text_1, y=user_input_text_2, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'line':
            fig = px.line(df, x=user_input_text_1, y=user_input_text_2, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'scatter':
            fig = px.scatter(df, x=user_input_text_1, y=user_input_text_2, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'box':
            fig = px.box(df, x=user_input_text_1, y=user_input_text_2, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Comparison')
        elif selected_chart == 'pie':
            fig = px.pie(df, names=user_input_text_1, labels={'x': 'X-axis'}, title='comparision')

    # Display the chart
    st.plotly_chart(fig)
