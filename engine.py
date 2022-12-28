import time
from turtle import Screen
from player import Player
from car_manager import CarManager, CAR_VELOCITY
from scoreboard import Scoreboard
from background_image import Background_Creator
from level import Level

class Engine():
    def __init__(self):
        self.screen = Screen()
        # self.screen.title('Keep your shell feeling well!')
        # self.screen.bgcolor("black")
        # self.screen.setup(width=600, height=600)
        # self.screen.tracer(0)
        #self.player = Player() - cannot call here and then not call again
        # self.background_image = Background_Creator()
        #self.car_manager = CarManager(self.screen) - cannot call here and then not call again
        #self.level = Level() -cannot call here and then not call again
        #self.scoreboard = Scoreboard() - cannot call here and then not call again
        # self.scoreboard.print_level(self.level.get_level())
        
    def reset_screen(self):
        self.screen.title('Keep your shell feeling well!')
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.player = Player()
        self.background_image = Background_Creator()
        self.car_manager = CarManager(self.screen)
        self.level = Level()
        self.scoreboard = Scoreboard()
        self.scoreboard.print_level(self.level.get_level())

    def run(self):
        game_is_on = True
        self.screen.listen()
        self.screen.onkeypress(self.player.move, "Up")
        last_time = time.perf_counter()
        time_since_last_car = time.perf_counter()
        while game_is_on:
            current_time = time.perf_counter()
            delta_time = current_time - last_time
            last_time = current_time
            self.screen.update()
            for car in self.car_manager.car_list:
                game_is_on = self.car_manager.collision_manager(self.player)
                # print(f"game_is_on = {game_is_on}")
                car.move(delta_time * self.level.get_car_velocity())
                self.car_manager.delete_old_cars()
            self.car_manager.delete_old_cars()
            if current_time - time_since_last_car > self.level.get_car_spawn_period():
                self.car_manager.add_car()
                time_since_last_car = current_time
        
            if self.player.ycor() >= 235:
                self.player.reset()
                self.level.increment_level()
                self.scoreboard.print_level(self.level.get_level())

        self.scoreboard.game_over()
        time.sleep(2)
        if self.level.level > self.level.best_score:
            self.level.best_score = self.level.level
            #scoreboard.beat_high_score()
        

    def main_loop(self):
        #play_again = False
        user_input = 'yes'
        while user_input == 'yes':
            if user_input == 'yes':
                self.screen.clear()
                self.reset_screen()
                self.run()
                user_input = self.screen.textinput(title = "One more time?", prompt = "Would you like to play again? Type 'yes' or 'no'".lower())

            else:
                #scoreboard.clear()
                self.scoreboard.end_message(self.level.level)

        self.screen.exitonclick()