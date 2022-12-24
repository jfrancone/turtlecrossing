import time
from turtle import Screen
from player import Player
from car_manager import CarManager, CAR_VELOCITY
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
scoreboard = Scoreboard()
loop_count = 0
last_time = time.perf_counter()
while game_is_on:
    # time.sleep(0.1)
    current_time = time.perf_counter()
    delta_time = current_time - last_time
    last_time = current_time
    screen.update()
    for car in car_manager.car_list:
        game_is_on = car_manager.collision_manager(player)
        # print(f"game_is_on = {game_is_on}")
        car.move(delta_time * CAR_VELOCITY)
        car_manager.delete_old_cars()
    car_manager.delete_old_cars()
    if loop_count >= 10:
        car_manager.add_car()
        loop_count = 0
    loop_count += 1
