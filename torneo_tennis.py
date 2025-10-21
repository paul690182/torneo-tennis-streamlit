
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Connessione al database
conn = sqlite3.connect("torneo_tennis.db")
c = conn.cursor()

# Funzione per aggiornare la classifica
def aggiorna_classifica(vincitore, perdente, punteggio):
    if punteggio == "2-0":
        c.execute("UPDATE classifica SET punti = punti + 3 WHERE giocatore = ?", (vincitore,))
    elif punteggio == "2-1":
        c.execute("UPDATE classifica SET punti = punti + 2 WHERE giocatore = ?", (vincitore,))
        c.execute("UPDATE classifica SET punti = punti + 1 WHERE giocatore = ?", (perdente,))
    elif punteggio == "1-2":
        c.execute("UPDATE classifica SET punti = punti + 1 WHERE giocatore = ?", (vincitore,))
        c.execute("UPDATE classifica SET punti = punti + 2 WHERE giocatore = ?", (perdente,))
    elif punteggio == "0-2":
        c.execute("UPDATE classifica SET punti = punti + 3 WHERE giocatore = ?", (perdente,))
    conn.commit()

# Titolo
st.title("Torneo di Tennis - Tutti contro Tutti")

# Sezione inserimento risultati
st.subheader("Inserisci Risultato")
c.execute("SELECT giocatore FROM classifica")
giocatori = [row[0] for row in c.fetchall()]

giocatore1 = st.selectbox("Giocatore 1", giocatori)
giocatore2 = st.selectbox("Giocatore 2", [g for g in giocatori if g != giocatore1])
punteggio = st.selectbox("Punteggio", ["2-0", "2-1", "1-2", "0-2"])

if st.button("Registra Risultato"):
    c.execute("INSERT INTO risultati (giocatore1, giocatore2, punteggio, data) VALUES (?, ?, ?, ?)",
              (giocatore1, giocatore2, punteggio, datetime.now().strftime("%Y-%m-%d %H:%M")))
    aggiorna_classifica(giocatore1, giocatore2, punteggio)
    st.success("Risultato registrato!")

# Sezione classifica
st.subheader("Classifica")
df_classifica = pd.read_sql_query("SELECT * FROM classifica ORDER BY punti DESC", conn)
st.dataframe(df_classifica)

# Sezione storico
st.subheader("Storico Risultati")
df_risultati = pd.read_sql_query("SELECT * FROM risultati ORDER BY data DESC", conn)
st.dataframe(df_risultati)
