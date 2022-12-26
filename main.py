import time
from turtle import Screen
from player import Player
from car_manager import CarManager, CAR_VELOCITY
from scoreboard import Scoreboard
from background_image import Background_Creator
from level import Level

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")
background_image = Background_Creator()
car_manager = CarManager(screen)

game_is_on = True
level = Level()
scoreboard = Scoreboard()
scoreboard.print_level(level.get_level())
last_time = time.perf_counter()
time_since_last_car = time.perf_counter()
while game_is_on:
    current_time = time.perf_counter()
    delta_time = current_time - last_time
    last_time = current_time
    screen.update()
    for car in car_manager.car_list:
        game_is_on = car_manager.collision_manager(player)
        # print(f"game_is_on = {game_is_on}")
        car.move(delta_time * level.get_car_velocity())
        car_manager.delete_old_cars()
    car_manager.delete_old_cars()
    if current_time - time_since_last_car > level.get_car_spawn_period():
        car_manager.add_car()
        time_since_last_car = current_time
    
    if player.ycor() >= 235:
        player.reset()
        level.increment_level()
        scoreboard.print_level(level.get_level())

scoreboard.game_over()
screen.exitonclick()

