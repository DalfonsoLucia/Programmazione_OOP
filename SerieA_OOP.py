# Definisci una classe SerieA che è instanziata con un unico attributo paese che è fissato ed è sempre Italia.
# Crea una sottoclasse Roma che eredita dalla classe SerieA; non definire nessun metodo o attributo nella sua suite.crea una istanza di
# Roma che assegnerai alla variabile squadra e verifica se squadra è una istanza della classe SerieA

class SerieA():
    def __init__(self):
        self.paese = "Italia"
        
    
class Roma(SerieA):
        pass

squadra = Roma()
print(isinstance(squadra, SerieA))

