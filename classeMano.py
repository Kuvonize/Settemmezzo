from classeCarta import *
from classeMazzo import Mazzo
import random

class Mano:
    def __init__(self, mazzo):
        self.mazzo = mazzo
        self.carte_in_mano=[]
        self.valore_totale=0
        self.matta=False
        self.valore_matta=0
        ##self.mazzo = Mazzo()
        self.sballato=False

    def aggiungi_carta(self):
        self.carte_in_mano.append(self.mazzo.dai_carta())
        self.calcola_valore()

    def svuota_mano(self):
        self.carte_in_mano.clear()

    def controllo_matta(self):
        for carta in self.carte_in_mano:
            if carta.rango == 'Re' and carta.seme == 'Oro':
                self.matta = True
                while self.matta:
                    try:
                        self.valore_matta = float(input('Hai preso la matta! Inserisci il valore della matta (da 0.5 a 7): '))
                        if self.valore_matta==0.5 or (self.valore_matta.is_integer() and 1 <= self.valore_matta <= 7):
                            self.matta = False
                    except ValueError:
                        print('Valore non valido, riprovare.')
                        
    def calcola_valore(self):
        self.valore_totale=0
        for carta in self.carte_in_mano:
            if self.valore_matta !=0:
                if len(self.carte_in_mano) == 1:
                    self.valore_totale = self.valore_matta
                    break
                else:    
                    self.valore_totale= (carta.valore + self.valore_matta)-0.5
                    break
            else:
                self.valore_totale += carta.valore        
        if self.valore_totale > 7.5:
            self.sballato=True
        #else:
            #print(f"Il valore della mano è: {self.valore_totale}")

        return self.sballato