seme=('Oro', 'Spade', 'Bastoni', 'Coppe')
rango=('Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Donna', 'Cavallo', 'Re')
valore={'Asso': 1, 'Due': 2, 'Tre': 3, 'Quattro': 4, 'Cinque': 5, 'Sei': 6, 'Sette': 7, 'Donna': 0.5, 'Cavallo': 0.5, 'Re': 0.5}

class Carta:
    def __init__(self, seme, rango):
        self.seme = seme
        self.rango = rango
        self.valore = valore[rango]

    def __str__(self):
        return f"{self.rango} di {self.seme}"
    
        

