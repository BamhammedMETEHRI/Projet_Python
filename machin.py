L = []
class test:
    def __init__(self,a=None,age=None,ville=None) :
        self.name = a
        L.append(self)
        self.age = age
        self.ville= ville
    def new(self):
        return test(a.name,a.age,a.ville)
    def affiche(self):
        print("name : ",self.name,"\nage=",self.age,"\nville = ",self.ville)

test("bob",50,"paris")
a=L[0]
b = a.new()
b.name='raoul'
a.affiche()
b.affiche()