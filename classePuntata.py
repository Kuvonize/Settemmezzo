class Puntata:
    def __init__(self):
        self.soldi_totali = 0
        self.scommessa= 0

    def soldi_in_tasca(self):
        try:
            self.soldi_totali= float(input('Inserisci i soldi che hai in tasca: '))
        except ValueError:
            print('Valore non valido, riprovare.')
            self.soldi_in_tasca()

    def punta_soldi(self):
        try:
            self.scommessa = float(input('Inserisci la scommessa: '))
        except ValueError:
            print('Valore non valido, riprovare.')
            self.punta_soldi()
        else:
            if self.scommessa > self.soldi_totali:
                print('Scommessa superiore ai soldi in tasca, riprovare.')
                self.punta_soldi()
            else:
                self.soldi_totali -= self.scommessa
                print(f'Scommessa accettata. Soldi rimanenti: {self.soldi_totali}')

    def vinta(self):
        self.soldi_totali += self.scommessa * 2
        print(f'Hai vinto! Soldi totali: {self.soldi_totali}')  

    def persa(self):
        self.soldi_totali -= self.scommessa
        print(f'Hai perso! Soldi totali: {self.soldi_totali}')
                    