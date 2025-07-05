from classeCarta import *
from classeMazzo import Mazzo
from classeMano import Mano
from classePuntata import Puntata
import random

class Gioco:
    def __init__(self,_mazzo,_mano_giocatore,_mano_banco,_puntata):
        self.mazzo = _mazzo
        #self.mazzo.mischia()
        self.mano_giocatore = _mano_giocatore
        self.mano_banco=_mano_banco
        self.puntata = _puntata
        self.chiamo=True

    def mostra_alcune_carte(self):
        print('\nMano del Banco')
        print('<Carta nascosta>')
        print("\nMano del Giocatore:", *self.mano_giocatore.carte_in_mano, sep='\n')
        print(f'Valore mano del Giocatore: {self.mano_giocatore.valore_totale}')

    def mostra_tutte_le_carte(self):
        print('\nMano del Banco', *self.mano_banco.carte_in_mano, sep='\n')
        print(f'Valore mano del Banco: {self.mano_banco.valore_totale}')
        print("\nMano del Giocatore:", *self.mano_giocatore.carte_in_mano, sep='\n')
        print(f'Valore mano del Giocatore: {self.mano_giocatore.valore_totale}')

    def chiami_o_stai(self):
        while self.chiamo==True:
            scelta=input('Vuoi chiamare o stare? (c/s): ').lower()
            if scelta[0] == 'c':
                self.mano_giocatore.aggiungi_carta()
                self.mano_giocatore.controllo_matta()
                self.mano_giocatore.calcola_valore()
                self.mostra_tutte_le_carte()
                if self.mano_giocatore.sballato:
                    self.chiamo=False             
            elif scelta[0] == 's':
                print('Hai deciso di stare')
                self.mano_giocatore.controllo_matta()
                self.mano_giocatore.calcola_valore()
                self.chiamo = False
            else:
                print('Scelta non valida, riprova.')       
    
    def logica_banco(self):
        if self.mano_giocatore.sballato == True:
            return
        while True:
            if self.mano_banco.valore_totale < 5:
                self.mano_banco.aggiungi_carta()
                self.mano_banco.controllo_matta()
                self.mano_banco.calcola_valore() 

            else:
                print('Il banco ha deciso di stare')
                self.mano_banco.controllo_matta()
                self.mano_banco.calcola_valore()
                break


    def giocatore_sballato(self):
        print('Hai sballato!')
        self.puntata.persa()
    def giocatore_vince(self):
        self.puntata.vinta()
    def banco_sballato(self):
        print('Il banco ha sballato!')
        self.puntata.vinta()
    def banco_vince(self):
        self.puntata.persa()
         