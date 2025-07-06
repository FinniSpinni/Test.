# gui_app.py

import streamlit as st
from Test import sortiere_text, get_ergebnisse, reset

st.title("📂 Ordnungssystem – Wörter & Zahlen sortieren")

eingabe = st.text_input("Gib Wörter/Zahlen ein (z. B. 'test 123 hallo 77')")

if st.button("Sortieren"):
    if eingabe.strip().lower() == "exit":
        st.info("👋 'exit' erkannt – Eingabe übersprungen.")
    else:
        sortiere_text(eingabe)

# Ergebnisse anzeigen
zahlen, woerter = get_ergebnisse()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔢 Zahlen")
    st.write(zahlen)

with col2:
    st.subheader("🅰️ Wörter")
    st.write(woerter)

# Reset-Funktion
if st.button("Zurücksetzen"):
    reset()
    st.success("Listen wurden zurückgesetzt.")
