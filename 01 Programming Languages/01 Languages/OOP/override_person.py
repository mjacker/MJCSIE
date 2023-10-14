from typing import override

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f'{self.name} is eating...')

    @override
    def work(self) -> None:
        print(f'{self.name} is working...')

class Programmer(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def work (self) -> None:
        print(f'{self.name} is programming...')

if __name__ == "__main__":
    Programmer = Programmer("MJacker")
    Programmer.work()