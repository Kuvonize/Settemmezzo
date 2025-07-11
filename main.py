from classeCarta import *
from classeMazzo import Mazzo
from classeMano import Mano
from classePuntata import Puntata
from classeGioco import Gioco
import random

if __name__=='__main__':
    partita_in_corso=True
    mazzo=Mazzo()
    mazzo.mischia()
    banco=Mano(mazzo)
    giocatore=Mano(mazzo)
    soldi=Puntata()
    soldi.soldi_in_tasca()
    print('Benvenuto in Sette e mezzo!')

    while partita_in_corso==True:
        banco.aggiungi_carta()
        giocatore.aggiungi_carta()

        partita=Gioco(mazzo,giocatore,banco,soldi)
        partita.mostra_tutte_le_carte()
        partita.puntata.punta_soldi()
        partita.chiami_o_stai()
        partita.logica_banco()

        partita.mostra_tutte_le_carte()

        if partita.mano_giocatore.sballato == True:
            partita.giocatore_sballato()
            partita_in_corso=False
        elif partita.mano_banco.sballato == False:
            partita.banco_sballato()      
        elif partita.mano_giocatore.calcola_valore() > partita.mano_banco.calcola_valore():
            partita.giocatore_vince()
            partita_in_corso=False
        elif partita.mano_giocatore.calcola_valore() <= partita.mano_banco.calcola_valore():
            partita.banco_vince()
            partita_in_corso=False    
        
        while True:
            x=input('Vuoi continuare a giocare?(si o no): ')
            if x[0].lower()=='s':
                partita_in_corso=True
                break
            elif x[0].lower()=='n':
                partita_in_corso=False
                break
            else:
                print('Scelta errata!')    
            