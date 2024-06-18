import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='Skandix Products', page_icon='🚗', initial_sidebar_state='expanded')
st.title('Skandix Products')
st.logo('https://www.skandix.com/_rsrc/css/img/icons.png')
st.sidebar.title('Filter Options')

dtypes = {f'Fitment {i}': str for i in range(1, 29)}
dtypes.update({'Volvo OE': str, 'Filename': str, 'Name': str, 'Category': str, 'Attributes': str, 'Skandix number': int})

df = pd.read_csv('skandix_products_new_.csv', dtype=dtypes)

with st.sidebar:
    volvoOE = st.multiselect('Volvo OE', df['Volvo OE'].unique(), key='volvoOE')
    name = st.multiselect('Name', df['Name'].unique(), key='name')
    category = st.multiselect('Category', df['Category'].unique(), key='category')
    fitment = st.text_input('Fitment', '', placeholder='Type Here...')
    filename = st.multiselect('Filename', df['Filename'].unique(), key='filename')

def search_fitment(df, fitments):
    for fitment in fitments:
        df = df[(df['Fitment 1'].str.contains(fitment, case=False, na=False)) | (df['Fitment 2'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 3'].str.contains(fitment, case=False, na=False)) | (df['Fitment 4'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 5'].str.contains(fitment, case=False, na=False)) | (df['Fitment 6'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 7'].str.contains(fitment, case=False, na=False)) | (df['Fitment 8'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 9'].str.contains(fitment, case=False, na=False)) | (df['Fitment 10'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 11'].str.contains(fitment, case=False, na=False)) | (df['Fitment 12'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 13'].str.contains(fitment, case=False, na=False)) | (df['Fitment 14'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 15'].str.contains(fitment, case=False, na=False)) | (df['Fitment 16'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 17'].str.contains(fitment, case=False, na=False)) | (df['Fitment 18'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 19'].str.contains(fitment, case=False, na=False)) | (df['Fitment 20'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 21'].str.contains(fitment, case=False, na=False)) | (df['Fitment 22'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 23'].str.contains(fitment, case=False, na=False)) | (df['Fitment 24'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 25'].str.contains(fitment, case=False, na=False)) | (df['Fitment 26'].str.contains(fitment, case=False, na=False))
                | (df['Fitment 27'].str.contains(fitment, case=False, na=False)) | (df['Fitment 28'].str.contains(fitment, case=False, na=False))]
    return df


if volvoOE:
    df = df[df['Volvo OE'].isin(volvoOE)]

if name:
    df = df[df['Name'].isin(name)]

if category:
    df = df[df['Category'].isin(category)]

if filename:
    df = df[df['Filename'].isin(filename)]

if fitment:
    df = search_fitment(df, fitment.split(' '))

df = df.dropna(axis=1, how='all')

st.dataframe(df, height=600)

