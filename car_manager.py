from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # how much the move speed increases when you level up
CAR_LANES = [-245, -215, -185, -155, -125, -95, -
             65, -35, -5, 25, 55, 85, 115, 145, 175, 205, 235]
CAR_SPEED = "slow"


class CarManager:

    def __init__(self):
        self.car_list = []
        self.create_starting_cars()

    def create_starting_cars(self):
        for y_pos in CAR_LANES:
            x = random.randint(-260, 270)
            car = Car(color=random.choice(COLORS),
                      position=(x, y_pos), speed=CAR_SPEED)
            self.car_list.append(car)

    def add_car(self):
        # add python time perf_counter
        rand_y = random.choice(CAR_LANES)
        last_car = self.car_list[-1]
        if last_car.ycor() == rand_y:
            rand_y = random.choice(CAR_LANES)
        car = Car(color=random.choice(COLORS),
                  position=(280, rand_y), speed=CAR_SPEED)
        self.car_list.append(car)

    def get_car_position(self):
        pass

    def delete_old_cars(self):
        for car in self.car_list:
            if car.xcor() < -300:
                car.reset()
                self.car_list.remove(car)
        print(self.car_list)

    def lane_checker(self, object):
        pass

    def collision_manager(self, player):
        for car in self.car_list:
            car_x = car.xcor()
            car_y = car.ycor()
            player_x = player.xcor()
            player_y = player.ycor()
            distance_x = abs(car_x - player_x)
            distance_y = abs(car_y - player_y)
            #print(f"car_x = {car_x} car_y =  {car_y}\nplayer_x = {player_x} player_y =  {player_y}\ndistance_x = {distance_x} distance_y = {distance_y}")
            if (distance_x < 6) and (distance_y < 6):
                print("Game over :(")
                return False
        return True


class Car(Turtle):
    def __init__(self, color, position, speed):
        super().__init__()
        self.setheading(180)
        self.shape("square")
        self.color(color)
        self.ht()
        self.penup()
        self.st()
        self.goto(position)

    def move(self):
        y = self.ycor()
        new_x = ((self.xcor()) - 10)
        self.goto(new_x, y)
