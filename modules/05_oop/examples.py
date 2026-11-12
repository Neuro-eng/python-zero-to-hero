from dataclasses import dataclass


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"


@dataclass
class Point:
    x: float
    y: float


for pet in [Animal("Generic"), Dog("Bruno")]:
    print(pet.speak())
print(Point(1, 2))
