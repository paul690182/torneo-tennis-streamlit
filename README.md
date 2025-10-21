
# Torneo Tennis - Tutti contro Tutti

Questa applicazione Streamlit consente a 12 giocatori di inserire i risultati delle partite e visualizzare la classifica e lo storico aggiornati in tempo reale.

## Funzionalità
- Inserimento risultati da qualsiasi postazione
- Classifica dinamica con punteggi
- Storico degli incontri visibile a tutti
- Salvataggio persistente su database SQLite

## Istruzioni
1. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
2. Avvia l'app:
   ```bash
   streamlit run torneo_tennis.py
   ```
3. Apri il link nel browser (es. http://localhost:8501)

## Regole Punteggio
- 2-0 → 3 punti al vincitore
- 2-1 → 2 punti al vincitore, 1 allo sconfitto
- 1-2 → 1 punto al vincitore, 2 allo sconfitto
- 0-2 → 3 punti allo sconfitto

