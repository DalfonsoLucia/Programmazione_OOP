# Il Poliformismo è la capacità di eseguire un'azione su un oggetto indipendentemente dal suo tipo
#spesso collegato con il termine duck typing:se cammina come una papera e fa qua qua come una papera, 
# è molto probabile che sia una papera.
# Permette al programma di fare uso di oggetti che espongono una stessa interfaccia, ma implementazioni diverse.
# Es.

class Animale():
    def __init__(self,specie):
        self.specie = specie 

    def razza(self):
        return f"Io sono della specie {self.specie}"


class Cane(Animale):
    def razza(self):
            return"bau bau"

class Gatto(Animale):
    def razza(self):
            return"miao"

c = Cane("pastore")

print(c.razza())

g = Gatto("persiano")

print(g.razza())

# il metodo razza si comporta in maniera diversa a seconda dell'istanza su cui viene chiamato
