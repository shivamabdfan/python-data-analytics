# running the dashboard 
# open the terminal 
# streamlit run dashboard.py
import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px


def load_data():
    # load the data
    df = pd.read_excel('data/Canada.xlsx', 
                   sheet_name=1,
                   skiprows=20, 
                   skipfooter=2)
    # rename the columns
    df = df.rename(columns={
        'OdName': 'country',
        'AreaName': 'continent',
        'RegName': 'region',
        'DevName': 'status',
    })
    # rename the values accordingly
    df = df.replace('United Kingdom of Great Britain and Northern Ireland','UK',)
    # drop unnecessary columns
    cols_to_drop = ['Type', 'Coverage', 'AREA', 'REG', 'DEV']
    df = df.drop(columns=cols_to_drop)
    # create a new column to display the total
    years = list(range(1980, 2014))
    df['total'] = df[years].sum(axis=1)
    df = df.set_index('country')
    return df # return the dataframe
st.set_page_config(
    page_icon="🌍",
    page_title="Immigration Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

years = list(range(1980, 2014))
df= load_data()
st.title("Immigration Analysis Dashboard")
st.subheader("United National data on international migration")
c1, c2 ,c3, c4= st.columns(4)
chosen_years=c1.multiselect('select years', years, help='select the years to find immigration data')
chosen_countries=c2.multiselect('Select Countries',df.index.tolist(),default=['India','China'],help='Select one or more country(ies)')
     
sort_order=c3.selectbox('sort order', ['Ascending', 'Descending'])

#visualization
if chosen_years and chosen_countries:
    filtered_df=df.loc[chosen_countries, chosen_years]
    if sort_order=="Ascending":
        filtered_df= filtered_df.sort_value(by=chosen_years,ascending=True)
    else:
        filtered_df= filtered_df.sort_values(by=chosen_years,ascending=False)
    st.dataframe(filtered_df)
    fig=px.line(filtered_df.T, x=filtered_df.columns,y=filtered_df.index)
    st.plotly_chart(fig, use_container_width=True)
    
        