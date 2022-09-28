# pandas
# streamlit
# csv file into pandas
# display dataframe using st.dataframe
import streamlit as st
import pandas as pd


# takes only the transaction date and net amount columns from the csv file
fields = ['Transaction Date', 'Net Amount']

df = pd.read_csv('Activities.csv', skipinitialspace=True, usecols=fields)

# prints the table in the link
st.dataframe(df)

df = df.set_index('Transaction Date')

# prints the graph in the link
st.bar_chart(df)

# prints the average in the link
total = 0.00

for i in df['Net Amount']:
    total += float(i)
    
average = total / len(df['Net Amount'])

st.write('The average dividend it $', round(average, 2))