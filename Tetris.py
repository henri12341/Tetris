import turtle
import time
import random

class Tetris():
    def __init__(self, window_height, window_width):
        self.fallen_pieces = []
        self.player_tetraminos = []
        self.window_height = window_height
        self.window_width = window_width
        self.current_shape = "square"
        self.rotation = 0

    def stop_tetraminos(self):
        height_values = []
        for tetramino in self.player_tetraminos:
            self.fallen_pieces.append(tetramino)
            height_values.append(tetramino.ycor())
        self.player_tetraminos = []
        self.check_full_line(height_values)
        self.new_random_tetramino_shape()

    def get_y_coordinate(self):
        lowest_y = 1000
        for tetramino in self.player_tetraminos:
            if tetramino.ycor() < lowest_y:
                lowest_y = tetramino.ycor()
        return lowest_y

    def new_square_tetramino(self):
        x = 0
        y = 0
        for i in range(0,4):
            if (i == 0):
                x = 0
                y = self.window_height/2-20
            elif (i == 1):
                x = 0
                y = self.window_height/2
            elif (i == 2):
                x = 20
                y = self.window_height/2-20
            else:
                x = 20
                y = self.window_height/2
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("blue")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_J_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = 0
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2 - 20
            elif (i == 2):
                x = 0
                y = self.window_height / 2 - 40
            else:
                x = -20
                y = self.window_height / 2 - 40
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("pink")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_L_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = 0
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2 - 20
            elif (i == 2):
                x = 0
                y = self.window_height / 2 - 40
            else:
                x = 20
                y = self.window_height / 2 - 40
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("orange")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_z_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = -20
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2
            elif (i == 2):
                x = 0
                y = self.window_height / 2 - 20
            else:
                x = 20
                y = self.window_height / 2 - 20
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("green")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_T_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = 20
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2
            elif (i == 2):
                x = -20
                y = self.window_height / 2
            else:
                x = 0
                y = self.window_height / 2 - 20
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("purple")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_s_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = 20
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2
            elif (i == 2):
                x = 0
                y = self.window_height / 2 - 20
            else:
                x = -20
                y = self.window_height / 2 - 20
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("red")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_i_shape_tetramino(self):
        x = 0
        y = 0
        for i in range(0, 4):
            if (i == 0):
                x = 0
                y = self.window_height / 2
            elif (i == 1):
                x = 0
                y = self.window_height / 2 - 20
            elif (i == 2):
                x = 0
                y = self.window_height / 2 - 40
            else:
                x = 0
                y = self.window_height / 2 - 60
            tetramino = turtle.Turtle()
            tetramino.speed(0)
            tetramino.shape("square")
            tetramino.pencolor("black")
            tetramino.fillcolor("cyan")
            tetramino.shapesize(0.95, 0.95, 1)
            tetramino.up()
            tetramino.goto(x, y)
            tetramino.down()
            tetramino.penup()
            self.player_tetraminos.append(tetramino)

    def new_tetramino(self):
        tetramino = turtle.Turtle()
        tetramino.speed(0)
        tetramino.shape("square")
        tetramino.color("green")
        tetramino.shapesize(0.95, 0.95)
        tetramino.up()
        tetramino.goto(0, 100)
        tetramino.down()
        tetramino.penup()
        self.player_tetraminos.append(tetramino)

    def new_random_tetramino_shape(self):
        """
        Shapes: square, I, s, z, L, J, T
        :return:
        """
        self.rototation = 0
        luku = random.randint(0,6)
        if (luku == 0):
            self.current_shape = "square"
            self.new_square_tetramino()
        if (luku == 1):
            self.current_shape = "I"
            self.new_i_shape_tetramino()
        if (luku == 2):
            self.current_shape = "s"
            self.new_s_shape_tetramino()
        if (luku == 3):
            self.current_shape = "z"
            self.new_z_shape_tetramino()
        if (luku == 4):
            self.current_shape = "L"
            self.new_L_shape_tetramino()
        if (luku == 5):
            self.current_shape = "J"
            self.new_J_shape_tetramino()
        if (luku == 6):
            self.current_shape = "T"
            self.new_T_shape_tetramino()



    def drop_tetramino_one_step(self):

        # Check that tetramino doesn't go out of window
        if (self.there_is_collision_with_fallen_pieces()):
            self.stop_tetraminos()
        elif (self.get_y_coordinate() < self.window_height/-2+40):
            self.stop_tetraminos()
        else:
            for tetramino in self.player_tetraminos:
                tetramino.goto(tetramino.xcor(), tetramino.ycor()-20)

    def there_is_collision_with_fallen_pieces(self):
        # Check collision with other tetraminos
        # Return true when there is collision with other pieces, false when not
        for fallen_tetramino in self.fallen_pieces:
            for player_tetramino in self.player_tetraminos:
                if ((player_tetramino.ycor()-20 == fallen_tetramino.ycor()) and
                player_tetramino.xcor() == fallen_tetramino.xcor()):
                    return True
        return False

    def move_right(self):
        for tetramino in self.player_tetraminos:
            tetramino.goto(tetramino.xcor()+20, tetramino.ycor())

    def move_left(self):
        for tetramino in self.player_tetraminos:
            tetramino.goto(tetramino.xcor() - 20, tetramino.ycor())

    def check_full_line(self, height_values):
        """
        Tarkistetaan aluksi kaikki tietyllä korkeudella olevat tetraminot
        Jos kappaleita kymmenen poistetaan rivit
        Jos poistetaan rivejä, pudetaan kaikki sitä suuremmalla korkeudella
        olevia kappaleita alaspäin
        :param height_values: contains height values that need to be checked
        :return:
        """
        removed_rows = 0
        min_height = min(height_values)
        for height_value in height_values:
            tetraminos_in_current_height = []
            for tetramino in self.fallen_pieces:
                if tetramino.ycor() == height_value:
                    tetraminos_in_current_height.append(tetramino)
            if (len(tetraminos_in_current_height) == 10):
                removed_rows += 1
                for tetramino in tetraminos_in_current_height:
                    self.fallen_pieces.remove(tetramino)
                    tetramino.hideturtle()

        for tetramino in self.fallen_pieces:
            if tetramino.ycor() > min_height:
                tetramino.goto(tetramino.xcor(), tetramino.ycor()-20*removed_rows)



def main():

    window_width = 400
    window_height = 400

    # Setup window
    window = turtle.Screen()
    window.title("Tetris")
    window.bgcolor("white")
    window.setup(window_width, window_height)
    window.tracer(0)

    tetris = Tetris(window_height, window_width)
    tetris.new_square_tetramino()

    # Set up controls
    window.listen()
    window.onkeypress(window.bye, "Escape")
    window.onkeypress(tetris.drop_tetramino_one_step, "Down")
    window.onkeypress(tetris.move_left, "Left")
    window.onkeypress(tetris.move_right, "Right")

    while True:
        window.update()
        tetris.drop_tetramino_one_step()

        time.sleep(0.2)


main()