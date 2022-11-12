import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background_image import Background_Creator

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")
background_image = Background_Creator()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    for car in car_manager.car_list:
        game_is_on = car_manager.collision_manager(player)
        # print(f"game_is_on = {game_is_on}")
        car.move()
    car_manager.delete_old_cars()
    car_manager.add_car()
