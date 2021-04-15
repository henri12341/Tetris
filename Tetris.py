import turtle
import time
import random

class Tetris():
    def __init__(self, window_height, window_width, window):
        self.window = window
        self.fallen_pieces = []
        self.player_tetraminos = []
        self.window_height = window_height
        self.window_width = window_width
        self.current_shape = "square"
        self.rotation = 0
        self.points = 0
        self.teksti = turtle.Turtle()
        self.teksti.penup()
        self.teksti.goto(125, -185)
        self.update_points()

    def update_points(self):
        self.teksti.clear()
        self.teksti.write("points: " + str(self.points))

    def game_over(self):
        for tetramino in self.fallen_pieces:
            tetramino.hideturtle()
        for tetramino in self.player_tetraminos:
            tetramino.hideturtle()
        self.player_tetraminos = []
        self.fallen_pieces = []
        main()


    def stop_tetraminos(self):
        height_values = []
        for tetramino in self.player_tetraminos:
            self.fallen_pieces.append(tetramino)
            if (tetramino.ycor() >= self.window_height/2):
                self.game_over()
            height_values.append(tetramino.ycor())
            height_values.append(tetramino.ycor()+20)
            height_values.append(tetramino.ycor()-20)

        self.player_tetraminos = []
        self.check_full_line(height_values)
        self.new_random_tetramino_shape()

    def get_highest_y_coordinate(self):
        highest_y = self.player_tetraminos[0].ycor()
        for tetramino in self.player_tetraminos:
            if tetramino.ycor() > highest_y:
                highest_y = tetramino.ycor()
        return highest_y

    def get_lowest_y_coordinate(self):
        """
        Returns lowest y-coordinate of player controlled pieces
        :return:
        """
        lowest_y = self.player_tetraminos[0].ycor()
        for tetramino in self.player_tetraminos:
            if tetramino.ycor() < lowest_y:
                lowest_y = tetramino.ycor()
        return lowest_y

    def get_highest_x_coordinate(self):
        highest_x = self.player_tetraminos[0].xcor()
        for tetramino in self.player_tetraminos:
            if (tetramino.xcor() > highest_x):
                highest_x = tetramino.xcor()
        return highest_x

    def get_lowest_x_coordinate(self):
        """
        returns lowest x-coordinate of player controlled pieces
        :return:
        """
        lowest_x = self.player_tetraminos[0].xcor()
        for tetramino in self.player_tetraminos:
            if (tetramino.xcor() < lowest_x):
                lowest_x = tetramino.xcor()
        return lowest_x

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
            self.current_shape = "S"
            self.new_s_shape_tetramino()
        if (luku == 3):
            self.current_shape = "Z"
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

    def turn_J_shape(self):
        self.rotation += 1
        if (self.rotation > 3):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # pystyssä
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 20, min_y + 40)
        elif (self.rotation == 1):
            # sivuttain
            self.player_tetraminos[0].goto(min_x + 40, min_y)
            self.player_tetraminos[1].goto(min_x + 40, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x, min_y + 20)
        elif (self.rotation == 2):
            # ylösalaisin
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x, min_y + 40)
            self.player_tetraminos[3].goto(min_x + 20, min_y + 40)
        elif (self.rotation == 3):
            # sivuttain
            self.player_tetraminos[0].goto(min_x, min_y + 20)
            self.player_tetraminos[1].goto(min_x, min_y)
            self.player_tetraminos[2].goto(min_x + 20, min_y)
            self.player_tetraminos[3].goto(min_x + 40, min_y)

    def turn_L_shape(self):
        self.rotation += 1
        if (self.rotation > 3):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # pystyssä
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x, min_y + 20)
            self.player_tetraminos[3].goto(min_x, min_y + 40)
        elif (self.rotation == 1):
            # sivuttain
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 40, min_y + 20)
        elif (self.rotation == 2):
            # ylösalaisin
            self.player_tetraminos[0].goto(min_x, min_y + 40)
            self.player_tetraminos[1].goto(min_x + 20, min_y + 40)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 20, min_y)
        elif (self.rotation == 3):
            # sivuttain
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x + 40, min_y)
            self.player_tetraminos[3].goto(min_x + 40, min_y + 20)

    def turn_t_shape(self):
        self.rotation += 1
        if (self.rotation > 3):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # vaakataso
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 40, min_y)
        elif (self.rotation == 1):
            # pystyssä
            self.player_tetraminos[0].goto(min_x + 20, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[2].goto(min_x, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 20, min_y + 40)
        elif (self.rotation == 2):
            # ylösalaisin
            self.player_tetraminos[0].goto(min_x + 20, min_y)
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 40, min_y + 20)
        elif (self.rotation == 3):
            # pystyssä
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x, min_y + 40)

    def turn_z_shape(self):
        self.rotation += 1
        if (self.rotation > 1):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # vaakataso
            self.player_tetraminos[0].goto(min_x, min_y + 20)
            self.player_tetraminos[1].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y)
            self.player_tetraminos[3].goto(min_x + 40, min_y)
        elif (self.rotation == 1):
            # pystyssä
            self.player_tetraminos[0].goto(min_x, min_y )
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 20, min_y + 40)

    def turn_s_shape(self):
        self.rotation += 1
        if (self.rotation > 1):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # vaakataso
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 40, min_y + 20)
        elif (self.rotation == 1):
            # pystyssä
            self.player_tetraminos[0].goto(min_x, min_y + 40)
            self.player_tetraminos[1].goto(min_x, min_y + 20)
            self.player_tetraminos[2].goto(min_x + 20, min_y + 20)
            self.player_tetraminos[3].goto(min_x + 20, min_y)

    def turn_I_shape(self):
        self.rotation += 1
        if (self.rotation > 1):
            self.rotation = 0

        min_x = self.get_lowest_x_coordinate()
        min_y = self.get_lowest_y_coordinate()

        if (self.rotation == 0):
            # Pystyssä
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x, min_y+20)
            self.player_tetraminos[2].goto(min_x, min_y+40)
            self.player_tetraminos[3].goto(min_x, min_y+60)
        elif (self.rotation == 1):
            # Vaakataso
            self.player_tetraminos[0].goto(min_x, min_y)
            self.player_tetraminos[1].goto(min_x + 20, min_y)
            self.player_tetraminos[2].goto(min_x + 40, min_y)
            self.player_tetraminos[3].goto(min_x + 60, min_y)



    def turn_tetramino(self):
        if (self.current_shape == "square"):
            pass
        elif (self.current_shape == "I"):
            self.turn_I_shape()
        elif (self.current_shape == "S"):
            self.turn_s_shape()
        elif (self.current_shape == "Z"):
            self.turn_z_shape()
        elif (self.current_shape == "T"):
            self.turn_t_shape()
        elif (self.current_shape == "L"):
            self.turn_L_shape()
        elif (self.current_shape == "J"):
            self.turn_J_shape()
        else:
            return

    def drop_tetramino_one_step(self):

        # Check that tetramino doesn't go out of window
        if (self.there_is_collision_with_fallen_pieces()):
            self.stop_tetraminos()
        elif (self.get_lowest_y_coordinate() < self.window_height / -2 + 40):
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
        # Check collision with other tetraminos
        for fallen_tetramino in self.fallen_pieces:
            for tetramino in self.player_tetraminos:
                if (tetramino.xcor() + 20 == fallen_tetramino.xcor()
                        and tetramino.ycor() == fallen_tetramino.ycor()):
                    return
        # Check collision with screen sides
        if (self.get_highest_x_coordinate() < 5*20):
            for tetramino in self.player_tetraminos:
                tetramino.goto(tetramino.xcor()+20, tetramino.ycor())

    def move_left(self):
        # Check collision with other teraminos
        for fallen_tetramino in self.fallen_pieces:
            for tetramino in self.player_tetraminos:
                if (tetramino.xcor() - 20 == fallen_tetramino.xcor()
                and tetramino.ycor() == fallen_tetramino.ycor()):
                    return
        # Check collision with screen sides
        if (self.get_lowest_x_coordinate() > (-5 * 20)):
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
            if (len(tetraminos_in_current_height) >= 11):
                removed_rows += 1
                for tetramino in tetraminos_in_current_height:
                    self.fallen_pieces.remove(tetramino)
                    tetramino.hideturtle()

        for tetramino in self.fallen_pieces:
            if tetramino.ycor() > min_height:
                tetramino.goto(tetramino.xcor(), tetramino.ycor()-20*removed_rows)
        self.points += removed_rows
        self.update_points()



def main():

    window_width = 400
    window_height = 400

    # Setup window
    window = turtle.Screen()
    window.title("Tetris")
    window.bgcolor("white")
    window.setup(window_width, window_height + 40) # extra margins
    window.tracer(0)


    tetris = Tetris(window_height, window_width, window)

    # Set up controls
    window.listen()
    window.onkeypress(window.bye, "Escape")
    window.onkeypress(tetris.drop_tetramino_one_step, "Down")
    window.onkeypress(tetris.move_left, "Left")
    window.onkeypress(tetris.move_right, "Right")
    window.onkeypress(tetris.turn_tetramino, "Up")

    screen = turtle.Turtle()
    screen.speed(0)
    screen.shape("square")
    screen.pencolor("black")
    screen.fillcolor("black")
    screen.shapesize(22, 12, 1)
    screen.up()
    screen.goto(0, 0)
    screen.down()
    screen.penup()


    tetris.new_square_tetramino()

    i = 0

    while True:
        window.update()
        i += 1
        if i == 100:
            tetris.drop_tetramino_one_step()
            i = 0


main()