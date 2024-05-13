class Dog:
    def __init__(self, name ,colour, age):
        self.name = name
        self.colour = colour
        self.age = age
    
    def bark(self):
        print(self.name, "BARKS")

dawa = Dog("Dawa","Brown",1)
nima = Dog("Nima", "Black",2)
blacky = Dog("Blacky", "Grey", 4)

print (dawa.name, dawa.colour, dawa.age)
print (nima.name, nima.colour, nima.age)
print (blacky.name, blacky.colour, blacky.age)
dawa.bark()