from classeCarta import *
import random

class Mazzo:
    def __init__(self):
        self.mazzo = []
        for semi in seme:
            for ranghi in rango:
                carta_creata=Carta(semi,ranghi)
                self.mazzo.append(carta_creata)  

    def __str__(self):
        mazzo_completo=''

        for carte in self.mazzo:
            mazzo_completo+= '\n'+carte.__str__()
        return 'Il mazzo ha: ' + mazzo_completo

    def mischia(self):
        random.shuffle(self.mazzo)

    def dai_carta(self):
        return self.mazzo.pop()

