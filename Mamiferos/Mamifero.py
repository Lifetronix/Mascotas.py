class Mamifero:
    def __init__(self,numlegsw):
        self.numlegsw=numlegsw
        self.drinkMilk=True
        self.borninMommy=True

    def isborning(self):
        born=True
        if born==True:
            print("The animal is mammal?")
            print(f"Yes is {born}")
        
        
perro=Mamifero(4)
perro.isborning()
print(perro.numlegsw)
