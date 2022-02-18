# Dichiara una classe Libro.
# Ogni istanza della classe dovrà avere pagine come attributo.
# Occorre definire anche due metodi speciali (dunder methods):
# - un metodo dovrà dare una rappresentazione delle nostre istanze quando le passiamo al metodo print() e 
# dovrà mostrare la stringa: "Libro di {x} pagine" dove x rappresenta il numero di pagine. 
# - il secondo metodo dovrà rappresentare la lunghezza del libro, cioè quando chiamiamo *len* su una istanza, 
# questa deve restituire il numero di pagine
# esempio:
# libro = Libro(100)
# print(libro) --> Libro di 100 pagine
# len(libro) --> 100

class Libro():

    def __init__(self, pagine):
        self.pagine = pagine

    def __str__(self):
        return f"Libro di '{self.pagine}' pagine"

    def __len__(self):
        return self.pagine

libro = Libro(100)
print(libro)

print(len(libro))


