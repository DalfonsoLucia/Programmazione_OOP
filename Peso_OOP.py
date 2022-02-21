class Peso():
    def __init__(self, peso): # suppongo che all'esterno si abbia solo concezione del peso in grammi
        self._chili = peso/1000 # _chili sarebbe un attributo privato

    def _get_grammi(self):  # metodo "protetto" di lettura (getter), destinato solo all'uso interno
        return self._chili*1000

    def _set_grammi(self, peso):    # metodo "protetto" di "scrittura (setter)", destinato solo all'uso interno
        if peso >= 0:
            self._chili = peso/1000
        else:
            self._chili = 0

    grammi = property(_get_grammi, _set_grammi) # la funzione accetta diversi argomenti, tutti opzionali,
                                                # di cui i primi due sono un metodo getter e setter

p = Peso(5000)

print(p.grammi) # la mia classe non ha nessuno attributo "grammi", tutto è codificato sottoforma di kg al suo interno
                # eppure sfruttando le properites riesco a mascherare *grammi* come un attributo (in realtà è una property)

p.grammi = -10000 # invoco il metodo setter della mia property

print(p.grammi)

#SCRITTURA ALTERNATIVA CON USO DI DECORATORI

class Peso():
    def __init__(self, peso): # suppongo che all'esterno si abbia solo concezione del peso in grammi
        self._chili = peso/1000 # # _chili sarebbe un attributo privato

    @property
    def grammi(self): # il nome scelto rappresenterà il nome dell'attriuto disponibile all'esterno (grammi)
        return self._chili*1000

    @grammi.setter
    def grammi(self, peso):
        if peso >= 0:
            self._chili = peso/1000
        else:
            self._chili = 0

p = Peso(5000)

print(p.grammi) # la mia classe non ha nessuno attributo "grammi", tutto è codificato sottoforma di kg al suo interno
                # eppure sfruttando le properites riesco a mascherare *grammi* come un attributo (in realtà è una property)

p.grammi = 10000 # invoco il metodo setter della mia property

print(p.grammi)