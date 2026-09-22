import streamlit as st
import pandas as pd

st.title("Karaktersnitt-kalkulator")
st.write("Legg inn fagene dine, så regnes snittet ut automatisk. F teller ikke med i snittet.")

verdi = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}

fag = st.data_editor(
    pd.DataFrame({"Fag": [""], "Karakter": ["A"], "Studiepoeng": [7.5]}),
    num_rows="dynamic",
    column_config={"Karakter": st.column_config.SelectboxColumn(options=list("ABCDEF"))},
)

tellende = fag[fag["Karakter"].isin(verdi)]
poeng = tellende["Studiepoeng"].sum()
if poeng > 0:
    snitt = (tellende["Karakter"].map(verdi) * tellende["Studiepoeng"]).sum() / poeng
    st.metric("Ditt snitt", f"{snitt:.2f}")
