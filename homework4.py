import os
import requests

os.makedirs("Lessons", exist_ok=True)
os.makedirs("HomeWorks", exist_ok=True)

# Создание файлов уроков
open("Lessons/lesson1.py", 'a').close()
open("Lessons/lesson2.py", 'a').close()


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__} с аргументами: {args} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger
def greet(name):
    print(f"Привет, {name}!")


greet("Алиса")


class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет действие.")

    def attack(self):
        print(f"{self.name} атакует!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:
                print(f"{self.name} успешно попал в цель!")
            else:
                print(f"{self.name} промахнулся!")
        else:
            print(f"{self.name} не может атаковать, нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил стрелы! Теперь у него {self.arrows} стрел.")

    def status(self):
        return f"Имя: {self.name}, HP: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)


archer = Archer("Леголас", 100, 10, 0.8)
archer.attack()
archer.rest()
print(archer.status())

response = requests.get("https://api.github.com")
print("Статус-код запроса к GitHub API:", response.status_code)

rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 5)
rect3 = rect1 + rect2

print(rect1)
print(rect2)
print(rect3)
