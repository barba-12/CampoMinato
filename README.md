# Campo Minato

Un'applicazione Python sviluppata con la libreria Tkinter che riproduce il classico gioco del Campo Minato. I giocatori devono scoprire tutte le celle del campo senza attivare le bombe.

## Caratteristiche

- **Tre livelli di difficoltà:** Facile, Medio e Difficile.
- **Timer integrato:** Tiene traccia del tempo impiegato.
- **Interfaccia grafica intuitiva:** Celle colorate per migliorare la leggibilità e il gameplay.
- **Segnalazione di vittoria o sconfitta:** Messaggi popup per indicare il risultato.
- **Modalità di gioco:** Possibilità di segnare bandierine per indicare potenziali bombe.

## Requisiti

- Python 3.x
- Libreria Tkinter (preinstallata con Python nella maggior parte delle distribuzioni)

## Installazione

1. Clona il repository:
   ```bash
   git clone <URL-del-tuo-repository>
   ```
2. Naviga nella directory del progetto:
   ```bash
   cd campo-minato
   ```
3. Esegui lo script:
   ```bash
   python campo_minato.py
   ```

## Come giocare

1. **Seleziona un livello di difficoltà:**

   - Facile: Griglia 10x10 con 10 bombe.
   - Medio: Griglia 18x18 con 40 bombe.
   - Difficile: Griglia 24x24 con 99 bombe.

2. **Scopri le celle:**

   - Clic sinistro per scoprire una cella.
   - Clic destro per piazzare o rimuovere una bandierina.

3. **Vinci il gioco:** Scopri tutte le celle senza attivare le bombe. Una vittoria mostrerà un'animazione con simboli di fiore 🌸.

4. **Perdi il gioco:** Clicca su una bomba. Tutte le bombe verranno rivelate con un simbolo di mina 💣.

## Struttura del codice

- **Funzioni principali:**
  - `main()`: Configura il gioco e avvia l'interfaccia grafica.
  - `crea_griglia()`: Crea la griglia di gioco.
  - `scopri_cella()`: Gestisce la logica di scoperta delle celle.
  - `bandierina()`: Gestisce l'inserimento e la rimozione delle bandierine.
  - `posizione_bombe()`: Posiziona casualmente le bombe evitando le celle iniziali.
  - `conta_bombe()`: Calcola il numero di bombe adiacenti a ogni cella.
  - `sconfitta()` e `vittoria()`: Gestiscono gli eventi di fine gioco.

## Personalizzazione

Puoi modificare la dimensione della griglia o il numero di bombe cambiando i parametri nella funzione `main()`:

```python
main(righe, colonne, altezza_celle, larghezza_celle, numero_bombe)
```
