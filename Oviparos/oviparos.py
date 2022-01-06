class Oviparous:
    def __init__(self,numlegsw):
        self.numlegsw=numlegsw
        self.drinkMilk=False
        self.borninMommy=False

    def isborning(self):
        born=True
        if born==True:
            print("The animal is oviparous?")
            print(f"Yes is {born} and borns from an egg")
    
    def isdying(self):
        born=False
        print("The animal is oviparous?")
        if born==True:
            print(f"Yes is {born} and borns from an egg")
        else:
            print(f"No is {born}")
        
pez = Oviparous(0)
pez.isborning()
print(pez.numlegsw)