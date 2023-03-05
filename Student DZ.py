import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")


    def live(self, day):
        day_str = f"Day {day} of {self.name}'s Life"
        print(f"{day_str:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
            self.to_sleep()
        elif live_cube == 2:
            self.to_chill()
            self.to_shopping
        elif live_cube == 3:
            self.to_work()
        self.end_of_day()

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False



nick = Student(name="Nick")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)

class Money:
    def __init__(self):
        self.money = 0
        self.gladness = 50
        self.progress = 0

    def to_work(self):
        print("Need to earn some money")
        self.gladness -= 2
        self.progress -= 1
        self.money += 5

    def to_shopping(self):
        print("I have money, I'll go buy myself something")
        self.gladness += 2
        self.progress -= 1
        self.money -= 10
class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def eat(self):
        print("Cat eating.")

    def sleep(self):
        print("Cat sleeping.")


class Cat(Pet):
    def __init__(self, name="Chester", age=5, breed="Siberian"):
        super().__init__(name, age, breed)