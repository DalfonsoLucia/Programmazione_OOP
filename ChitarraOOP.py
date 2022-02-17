class Chitarra():
    def __init__(self, modello, marca, numero_corde = 6):
        self.modello = modello
        self.marca = marca
        self.numero_corde = numero_corde

c1 = Chitarra("Telecaster", "Fender")
c2 = Chitarra("Telecaster", "Fender", 7)

print(c1.modello, c1.marca, c1.numero_corde)
print(c2.modello, c2.marca, c2.numero_corde)