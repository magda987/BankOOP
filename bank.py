class Bank:
    
    isNational = False

    def __init__(self, n):
        self.name = n

    def __str__(self):
        return f"Bank {self.name}"

    @classmethod   
    def setNat(cls, newNat):
        cls.isNational=newNat


seb = Bank("SEB")
print(seb)

seb.setNat(False)

print(seb.isNational)

# name= "SEB" zmienna/atrybut
# x= Bank() objekt/instancja
# metoda specjalna/magiczna __init__(self)
# self przechowuje instancjee

#atrybuty przypisane do kalsy lub do instancji

#metoda
