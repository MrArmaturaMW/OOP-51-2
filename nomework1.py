class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10


hero1 = Hero("Алекс", 5, 100)
hero1.introduce()

hero2 = Hero("Герой1", 12, 150)
hero3 = Hero("Герой2", 8, 90)
hero4 = Hero("Герой3", 15, 200)

print(hero2.name, "взрослый?", hero2.is_adult())
print(hero3.name, "взрослый?", hero3.is_adult())
print(hero4.name, "взрослый?", hero4.is_adult())