class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


monkey = Mammal()
print(isinstance(monkey, Animal))
print(issubclass(Mammal, Animal))
print(isinstance(monkey, object))
print(issubclass(Mammal, object))
