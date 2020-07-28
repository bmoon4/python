class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # 이게 없으면 parent 클래스의 생성자가 호출안된다.
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 0.5

    def swim(self):
        print("swim")


monkey = Mammal()
tuna = Fish()

print(monkey.age)
print(monkey.weight)

print(tuna.age)
print(tuna.weight)
