# Sette e mezzo

Gioco di carte **Sette e mezzo** da riga di comando, scritto in Python con la programmazione a oggetti. Giochi contro il banco puntando soldi virtuali.

## Regole implementate

- Mazzo da 40 carte napoletane (Oro, Spade, Bastoni, Coppe).
- Le carte dall'Asso al Sette valgono il loro numero; Donna, Cavallo e Re valgono mezzo punto.
- Il **Re di Oro è la matta**: chi la pesca sceglie quanto vale (0,5 oppure un intero da 1 a 7).
- Chi supera 7 e mezzo sballa e perde.
- Il banco pesca finché ha meno di 5 punti, poi sta.
- A parità di punteggio vince il banco.

## Come si gioca

1. Inserisci i soldi che hai a disposizione.
2. Vedi le tue carte (quella del banco resta coperta) e fai la puntata.
3. Scegli se chiamare un'altra carta (c) o stare (s).
4. Il banco gioca la sua mano e si confrontano i punteggi.
5. Puoi giocare un'altra mano o uscire.

## Avvio

Serve Python 3, nessuna libreria esterna:

    python main.py

## Struttura del codice

| File | Contenuto |
| --- | --- |
| classeCarta.py | Classe Carta: seme, rango e valore |
| classeMazzo.py | Classe Mazzo: crea le 40 carte, mescola e distribuisce |
| classeMano.py | Classe Mano: carte in mano, calcolo del punteggio, gestione della matta |
| classePuntata.py | Classe Puntata: soldi disponibili, scommessa, vincite e perdite |
| classeGioco.py | Classe Gioco: turno del giocatore, logica del banco, esito della mano |
| main.py | Ciclo principale della partita |
