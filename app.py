import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='Skandix Products', page_icon='🚗', initial_sidebar_state='expanded')
st.title('Skandix Products')
st.logo('https://www.skandix.com/_rsrc/css/img/icons.png')
st.sidebar.title('Filter Options')

# df = pd.read_csv('Work Svenska kategorier JJ .csv', dtype={'Volvo OE': str})
df = pd.read_csv('all_volvo.csv', dtype={'Volvo OE': str})
df_edit = df.copy()
# df.to_csv('filtered_data.csv', index=False)

with st.sidebar:
    volvoOE = st.multiselect('Volvo OE', df['Volvo OE'].unique(), key='volvoOE')
    Namn = st.multiselect('Namn', df['Namn'].unique(), key='Namn')
    Kategori = st.multiselect('Kategori', df['Kategori'].unique(), key='Kategori')
    Huvudkategori = st.multiselect('Huvudkategori', df['Huvudkategori'].unique(), key='Huvudkategori')
    Dubbla_kategorier = st.multiselect('Dubbla kategorier', df['Dubbla kategorier'].unique(), key='Dubbla kategorier')
    model = st.multiselect('Model', df['Model'].unique(), key='model')
    model_year = st.multiselect('Model Year', df['Model_Year'].unique(), key='model_year')
    engine_type = st.multiselect('Engine Type', df['Engine_Type'].unique(), key='engine_type')
    Combined_Attributes = st.multiselect('Combined_Attributes', df['Combined_Attributes'].unique(), key='Combined_Attributes')
    Priskategori = st.multiselect('Priskategori', df['Priskategori'].unique(), key='Priskategori')
    Unnamed_8 = st.multiselect('Unnamed: 8', df['Unnamed: 8'].unique(), key='Unnamed: 8')
    Unnamed_9 = st.multiselect('Unnamed: 9', df['Unnamed: 9'].unique(), key='Unnamed: 9')

if volvoOE:
    df_edit = df_edit[df_edit['Volvo OE'].isin(volvoOE)]

if model:
    df_edit = df_edit[df_edit['Model'].isin(model)]

if Namn:
    df_edit = df_edit[df_edit['Namn'].isin(Namn)]

if Kategori:
    df_edit = df_edit[df_edit['Kategori'].isin(Kategori)]

if Huvudkategori:
    df_edit = df_edit[df_edit['Huvudkategori'].isin(Huvudkategori)]

if Dubbla_kategorier:
    df_edit = df_edit[df_edit['Dubbla kategorier'].isin(Dubbla_kategorier)]

if Priskategori:
    df_edit = df_edit[df_edit['Priskategori'].isin(Priskategori)]

if Unnamed_8:
    df_edit = df_edit[df_edit['Unnamed: 8'].isin(Unnamed_8)]

if Unnamed_9:
    df_edit = df_edit[df_edit['Unnamed: 9'].isin(Unnamed_9)]

if model_year:
    df_edit = df_edit[df_edit['Model Year'].isin(model_year)]

if engine_type:
    df_edit = df_edit[df_edit['Engine Type'].isin(engine_type)]

if Combined_Attributes:
    df_edit = df_edit[df_edit['Combined Attributes'].isin(Combined_Attributes)]

df_edit = df_edit.dropna(axis=1, how='all')

df_edit = st.data_editor(df_edit)

if st.button('Save Filtered Data'):
    if not volvoOE and not model and not Namn and not Kategori and not Huvudkategori and not Dubbla_kategorier and not model_year and not engine_type and not Combined_Attributes and not Priskategori and not Unnamed_8 and not Unnamed_9:
        df_edit.to_csv('all_volvo.csv', index=False)
    else:
        for index, row in df_edit.iterrows():
            for col in df_edit.columns:
                if df_edit.loc[index, col] != df.loc[index, col]:
                    df.loc[index, col] = df_edit.loc[index, col]

        df.to_csv('all_volvo.csv', index=False)
