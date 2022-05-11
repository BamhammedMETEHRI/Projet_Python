#La classe des itème son la class des objet
class Item:
    def __init__(self,name,effect) :
        self.name=name
        if effect == "pokeball" :
            self.effect= "objet qui permer d'atraper un pokèmon"
            self.value = None
            self.prix = 5
        else:
            self.effect= "objet qui soigne les pokèmon"
            self.value = 10
            self.prix = 10
    #------------------------------------------------------------------