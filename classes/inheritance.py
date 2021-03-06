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
monkey.walk()
monkey.eat()
print(f"this monkey's age is {monkey.age}")

tuna = Fish()
tuna.swim()
tuna.eat()
print(f"this tuna's age is {tuna.age}")
