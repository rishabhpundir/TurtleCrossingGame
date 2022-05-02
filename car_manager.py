from turtle import Turtle
import random


COLORS = ['red', 'blue', 'green', 'violet', 'yellow', 'pink', 'grey', 'black', 'orange']
START_SPEED = 5
SPEED_INCR = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_SPEED
        

    def car_gen(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-260, 260)
            car.goto(300, random_y)
            self.all_cars.append(car)


    def car_move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)


    def level_up(self):
        self.car_speed += SPEED_INCR