import turtle
import time

class Tetris():
    def __init__(self, window_height, window_width):
        self.fallen_pieces = []
        self.player_tetraminos = []
        self.window_height = window_height
        self.window_width = window_width

    def stop_tetraminos(self):
        for tetramino in self.player_tetraminos:
            self.fallen_pieces.append(tetramino)
        self.player_tetraminos = []
        self.new_square_tetramino()

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

    def drop_tetramino_one_step(self):

        # Check that tetramino doesn't go out of window
        if (self.there_is_collision_with_fallen_pieces()):
            self.stop_tetraminos()
        if (self.get_y_coordinate() < self.window_height/-2+40):
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