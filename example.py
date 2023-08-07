import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import time

st.title("App - Visuals")
 
df_load = st.file_uploader("Select Your Local dataset CSV (default provided)")

@st.cache_data()
def load_file(df_load):
    time.sleep(3)
    if df_load is not None:
        df = pd.read_csv(df_load)
    else:
        df = st.markdown("Please, load your dataset")
    return(df)

df_load = load_file(df_load)
st.markdown("Dataset")
st.write(df_load.head())

st.markdown("Statics")
st.write(df_load.describe())


st.markdown("Scatterplot") 
selected_x_var = st.selectbox(
    "What do want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
 
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
)

selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male penguins', 'female penguins'])
if selected_gender == 'male penguins':
    df_load = df_load[df_load['sex'] == 'male']
elif selected_gender == 'female penguins':
    df_load = df_load[df_load['sex'] == 'female']
else:
    pass 

alt_chart = (
    alt.Chart(df_load, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
