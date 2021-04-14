import turtle
import time

class Tetris():
    def __init__(self, window_height, window_width, window):
        self.window_height = window_height
        self.window_width = window_width
        self.window = window
        self.board = []
        for y in range(0, 20):
            width = []
            for x in range(0, 10):
                width.append(x)
            self.board.append(width)
        print(self.board)
        self.board[2][2] = 1
        self.board[19][9] = 1

    def draw_board(self):
        self.window.clear()
        x = 0
        y = 0
        for table in self.board:
            for tetramino in table:
                tetramino = turtle.Turtle()
                tetramino.speed(0)
                tetramino.shape("square")
                tetramino.pencolor("black")
                tetramino.fillcolor("blue")
                tetramino.shapesize(0.95, 0.95, 1)
                tetramino.up()
                tetramino.goto(x*20, y*20)
                tetramino.down()
                tetramino.penup()
                x += 1
            y += 1
            x = 0


def main():

    window_width = 400
    window_height = 400

    # Setup window
    window = turtle.Screen()
    window.title("Tetris")
    window.bgcolor("white")
    window.setup(window_width, window_height)
    window.tracer(0)

    tetris = Tetris(window_height, window_width, window)

    # Set up controls
    window.listen()
    window.onkeypress(window.bye, "Escape")


    while True:
        window.update()
        tetris.draw_board()
        time.sleep(0.2)


main()