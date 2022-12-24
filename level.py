from turtle import Turtle

VELOCITY_PER_LEVEL = 30
CAR_SPAWN_RATE = 1
class Level(Turtle):
    def __init__(self):
        self.level = 1
        self.car_velocity = 0
        self.set_car_velocity()
        self.car_spawn_period = 1
        self.set_car_spawn_period()

    def increment_level(self):
        self.level += 1
        self.set_car_spawn_period()
        self.set_car_velocity()

    def get_level(self):
        return self.level

    def set_car_velocity(self):
        self.car_velocity = self.level * VELOCITY_PER_LEVEL
    
    def get_car_velocity(self):
        return self.car_velocity

    def set_car_spawn_period(self):
        self.car_spawn_period = CAR_SPAWN_RATE / self.level
    
    def get_car_spawn_period(self):
        return self.car_spawn_period
