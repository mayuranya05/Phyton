class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} year old".format(self.name, self.age)
    
    def speark(self, sound):
        return "{} is {} years old".format(self.name, sound)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
jim = Bulldog("Jim", 12)
print(jim.description())

print(jim.run("slowly"))

print(isinstance(jim, Dog))

juile = Dog("Julie", 100)
print(isinstance(juile, Dog))

johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

print(isinstance(juile, jim))