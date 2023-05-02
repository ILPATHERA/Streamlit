import streamlit as st
import pandas as pd
import altair as alt

# Header
st.set_page_config(page_title="Simone's Kalorienrechner", page_icon="🍎", layout="centered", initial_sidebar_state="auto")
st.header("Kalorienrechner")

# Formular
st.subheader("Damit wir Ihren Grundbedarf berechnen können, benötigen wir einige Angaben von Ihnen.")
username = st.text_input("Geben Sie hier Ihren Namen ein")
input0 = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
input1 = st.slider("Alter", min_value=0, max_value=120, step=1)
input2 = st.slider("Gewicht", min_value=0, max_value=150, step=1)
input3 = st.slider("Grösse", min_value=0, max_value=220, step=1)
input4 = st.slider("Training pro Woche", min_value=0, max_value=7, step=1)

# Button hinzufügen
if st.button("Berechnen"):
    # Grundbedarf berechnen
    if input0 == "Männlich":
        sum_inputsMale = 66.47 + (13.7 * input2) + (5 * input3) - (6.8 * input1)
        st.write(f"<h2>{username}'s Kaloriengrundbedarf ist: {sum_inputsMale:.2f}</h2>", unsafe_allow_html=True)
    else:
        sum_inputsFemale = 655.1 + (9.6 * input2) + (1.8 * input3) - (4.7 * input1)
        st.write(f"<h2>{username}'s Kaloriengrundbedarf ist: {sum_inputsFemale:.2f}</h2>", unsafe_allow_html=True)


df = pd.DataFrame({
    'Lebensmittel':  ["Ei", "Poulet", "Spinat", "Reis"],
    'Kalorien (kcal)': [142,130,168,23],
    'Protein (g)': [11,3,19,3],
    'Fett (g)': [10,0,10,0],
    'Kohlenhydrate (g)': [0,30,0,3],
})

st.write(df)

# Daten in lange Form bringen
df_long = pd.melt(df, id_vars=["Lebensmittel"])

# Grafik erstellen
chart = alt.Chart(df_long).mark_bar().encode(
    x='value:Q',
    y=alt.Y('Lebensmittel:N', sort='-x'),
    color='variable:N'
)

# Grafik anzeigen
st.altair_chart(chart, use_container_width=True)
