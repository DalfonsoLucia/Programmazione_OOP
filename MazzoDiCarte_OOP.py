# ESERCIZIO MAZZO DI CARTE
# Dobbiamo creare due classi:Carta e Mazzo
# per la classe Carta:
# Ogni istanza deve avere un seme ("Bastoni", "Coppe", "Denari" e "Spade")
# Ogni istanza deve avere un valore("A", "2", "3", "4", "5", "6", "7", "8", "9", "10")
# dunder method repr deve restituire il valore della carta e il suo seme ("2 di Denari", "A di Bastoni", ..)
# per la classe Mazzo:
# ogni istanza deve avere un attributo con tutte le possibili 40 combinazioni delle istanze della classe Carta
# un metodo di istanza conta che deve restituire il numero delle carte rimanenti nel mazzo
# Dunder method repr che deve restituire informazioni su quante carte sono rimaste nel mazzo ( "Mazzo di 40 carte", "Mazzo di 5 carte", ...)
# Un metodo protetto di istanza chiamato _distribuisci che accetta un numero e rimuove quel numero di carte dal mazzo 
# (fai attenzione a considerare i casi in cui provi a rimuovere più carte diquelle rimaste del mazzo). 
# Se nel mazzo sono rimaste 0 carte e provi a rimuovere delle carte, 
# questo metodo deve restituire un ValueError con il messaggio: "Non ci sono più carte nel mazzo"
# un metodo di istanza chiamato mischia che deve mischiare (usa la funzione shuffle di random) 
# il mazzo di carte e restituire il mazzo di carte mischiato, ma solo se questo ha tutte le 40 carte,
# altrimenti se alcune carte sono state già distribuite, se provi a chiamare questo metodo, 
# devi lanciare una eccezione, un ValueError con il messaggio: "Posso mischiare solo il mazzo con tutte le carte"
# Un metodo di istanza distribuisci_carta che sfrutta il metodo distribuisci per distribuire una carta dal mazzo e restituire quella carta
# Un metodo di istanza distribuisci_mano che riceve un numero come parametro e sfrutta il metodo distribuisci per distribuire un
# numero di carte dal mazzo e restituire la lista delle cartedistribuite

from random import shuffle

class Carta():
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def __repr__(self):
        return f"{self.valore}' di '{self.seme}"

class Mazzo():
    def __init__(self):
        semi = ["Bastoni", "Coppe", "Denari", "Spade"]
        valori = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.carte = [Carta(seme, valore) for seme in semi for valore in valori]
        # QUESTA E' LA VERSIONE ESTESA DELLA LIST COMPHENSION DI CUI SOPRA
        #Carta(seme, valore)
        #for seme in semi:
        #    for valore in valori:
      
    def conta(self):
        return len(self.carte)

    def __repr__(self):
        return f"Mazzo di {self.conta()} carte"

    def _distribuisci(self, num):
        count = self.conta()
        n_carte_da_distribuire = min([count, num])
        if count == 0:
            raise ValueError("Non ci sono carte nel mazzo")
        self.carte = self.carte[:-n_carte_da_distribuire]
        carte = self.carte[-n_carte_da_distribuire:]
        return carte

    def mischia(self):
        if self.conta() < 40:
            raise ValueError("Posso mischiare solo il mazzo con tutte le carte")
        shuffle(self.carte)
        
    def distribuisci_carta(self):
        return self._distribuisci(1)[0]

    def distribuisci_mano(self,num):
        return self._distribuisci(num)



m = Mazzo()
print("\n" + "Sto stampando le 40 carte del mazzo"+ "\n")
print(m.carte)
m.mischia()
print("\n" + "Sto stampando le 40 carte del mazzo tutte mischiate" + "\n")
print(m.carte)
carta = m.distribuisci_carta()
print("\n" + "Sto stampando la carta presa dal mazzo"+ "\n")
print(carta)
print("\n" + "Sto stampando la mano distribuita"+ "\n")
mano = m.distribuisci_mano(5)
print(mano)
#m.mischia() 
#print(m.carte) NON POSSO CHIAMARE m.mischia() E POI STAMPARE m.carte PERCHE' ALTRIMENTI AVREMO IL ValueError DELLA RIGA 38.


#USEREMO QUESTO ESEMPIO DELLO SLICING PER CAPIRE MEGLIO LA FUNZIONE _distribuisci()
# n = 3 # n è il numero che vogliamo prendere 
# mazzo = ["A","2","3","4","5","6","7","8","9","10"] # data la lista mazzo di carte
# carte_da_distribuire = mazzo[-n:] #qui lo slicing dice di prendere gli ultimi 3 elementi della lista
# print(carte_da_distribuire)
# rimanenti = mazzo[:-n] #qui lo slicing dice di prendere i primi 7 elementi della lista ovvero da zero a -3
# print(rimanenti)
