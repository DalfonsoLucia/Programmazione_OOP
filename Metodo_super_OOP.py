# super(): COME DELEGARE ALLA CLASSE BASE
# Perchè viene utilizzato il metodo super()?
# prendiamo l'esempio che segue:

class Animale():
    def __init__(self,specie):
        self.specie = specie 

    def razza(self):
        return f"Io sono della specie {self.specie}"


class Cane(Animale):
    def __init__(self, specie, pelo):
        self.specie = specie # è una duplicazione della linea 3, non è la soluzione migliore
        self.pelo = pelo

    def razza(self):
            return"bau bau"

# L'idea è quella di utilizzare le classi figlie per estendere le funzionalità della clase base e delegare alla classe base tutti 
# quegli aspetti tipici di una data famiglia di classi (Animali in questo esempio),
# altrimenti vanifichiamo l'intero concetto di ereditarietà

class Animale():
    def __init__(self,specie):
        self.specie = specie 

    def razza(self):
        return f"Io sono della specie {self.specie}"


class Cane(Animale):
    def __init__(self, specie, pelo):
        super().__init__(specie) # super() equivale ad una chiamata alla classe superiore (Animale)
        self.pelo = pelo
        super().razza()

    def razza(self):
            return"bau bau"

c = Cane("cane", pelo = "corto") # sto chidedno a python di invocare il metodo init,
                                 #li trova super() che è un modo per chiedere a python
                                 # di invocare il metodo init definito nella superclass (Animale)

# Ecco a cosa serve il metodo super() serve per non vanificare il concetto di ereditarietà 
# e di incappare nel meccanismo dell'overide.