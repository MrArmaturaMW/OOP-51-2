import os
import requests

os.makedirs("Lessons", exist_ok=True)
os.makedirs("HomeWorks", exist_ok=True)

open("Lessons/lesson1.py", 'a').close()
open("Lessons/lesson2.py", 'a').close()


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


archer = Archer("Леголас", 100, 10, 0.8)
archer.attack()
archer.rest()
print(archer.status())

response = requests.get("https://api.github.com")
print("Статус-код запроса к GitHub API:", response.status_code)
