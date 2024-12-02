import streamlit as st
import pandas as pd
import altair as alt

# Your data (cleaned up the extra spaces and colons)
data = {
    "Jahr": ["2002", "2022"],
    "Belgium": ["77.667", "73.950"],
    "Bulgaria": ["46.917", "37.132"],
    "Czechia": ["26.204", "41.793"],
    "Denmark": ["-42.287", "42.867"],
    "Germany": ["60.126", "68.555"],
    "Estonia": ["32.107", "6.159"],
    "Ireland": ["88.087", "79.155"],
    "Greece": ["71.063", "79.601"],
    "Spain": ["78.642", "74.347"],
    "France": ["50.817", "51.917"],
    "Croatia": ["54.450", "60.303"],
    "Italy": ["85.589", "79.165"],
    "Cyprus": ["100.557", "92.018"],
    "Latvia": ["58.760", "38.747"],
    "Lithuania": ["40.610", "72.434"],
    "Luxembourg": ["98.610", "91.317"],
    "Hungary": ["56.885", "64.183"],
    "Malta": ["99.802", "99.009"],
    "Netherlands": ["35.084", "80.266"],
    "Austria": ["68.022", "74.454"],
    "Poland": ["11.439", "46.029"],
    "Portugal": ["84.162", "71.274"],
    "Romania": ["24.275", "32.412"],
    "Slovenia": ["49.749", "53.966"],
    "Slovakia": ["64.476", "69.630"],
    "Finland": ["52.360", "40.884"],
    "Sweden": ["37.664", "26.824"],
    "Iceland": ["28.813", None], 
    "Bosnia and Herzegovina": [None, "26.281"], 
    "Montenegro": [None, "29.089"],
    "Moldova": [None, "81.000"],
    "North Macedonia": ["46.368", "63.022"],
    "Georgia": [None, "77.696"],
    "Albania": ["53.360", "31.467"],
    "Serbia": ["26.366", "44.902"],
    "Türkiye": ["67.567", "67.256"]
}

df = pd.DataFrame(data)

# Melt the DataFrame to long format for Altair
df_melted = df.melt(id_vars='Jahr', var_name='Country', value_name='Value')

# Convert 'Value' column to numeric
df_melted['Value'] = pd.to_numeric(df_melted['Value'])

# Streamlit app
st.title(':material/oil_barrel: Energieimporte und Importabhängigkeit')
st.markdown('Prozentualer Anteil der Nettoeinfuhren an der verfügbaren Bruttoenergie (basierend auf Terajoule) im Vergleich für die Jahre 2002 und 2022:')

# Auswahl der Länder
selected_countries = st.multiselect(
    'Wähle Länder aus:', 
    df_melted['Country'].unique(), 
    default=['Germany']
)

# Filter die Daten basierend auf der Auswahl
filtered_df = df_melted[df_melted['Country'].isin(selected_countries)]

# Create the Altair chart
chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x='Jahr',
    y=alt.Y('Value', title='Prozentualer Anteil'),
    color='Country',
    tooltip=['Jahr', 'Country', 'Value']
).properties(
    title='Abhängigkeit von Energieimporten - gesamt',
).interactive()

container = st.container(border=True)

container.altair_chart(chart, use_container_width=True)

st.markdown('Die EU ist in hohem Maße von Energieimporten abhängig, insbesondere von fossilen Brennstoffen. Die Abhängigkeit von Russland als Energielieferant ist ein Risikofaktor, der durch den Krieg in der Ukraine deutlich wurde. Die EU-Länder weisen unterschiedliche Abhängigkeiten auf, wobei einige Länder fast vollständig auf Importe angewiesen sind.')

with st.expander("Quellen"):
    st.link_button('Eurostat',"https://ec.europa.eu/eurostat/de/web/interactive-publications/energy-2024")