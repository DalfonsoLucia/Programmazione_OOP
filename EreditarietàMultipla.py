class A():
    def saluta(self):
        return "ciao"

    def presenta(self):
        return "Io sono classe A"
    
class B():
    def chiama(self):
        return "vieni qua"

    def presenta(self):
        return "Io sono classe B"

class C(B,A):
    pass

c = C()
print(c.presenta())
