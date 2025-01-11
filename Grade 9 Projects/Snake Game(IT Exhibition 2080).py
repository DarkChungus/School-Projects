from tkinter import *
import random

score = 0
screen_width = 600
screen_height = 600
speed = 69
parts_size = 50
snake_parts = 3
snake_color = "#004F00"  # by the way, this color is called "dumpster" no joke
food_color = "#BE2625"
bg_color = "#000000"


class ObjectSnake:

    def __init__(self):
        self.size = snake_parts
        self.coords = []
        self.squares = []

        for i in range(0, snake_parts):
            self.coords.append([0, 0])

        for x, y in self.coords:
            square = screen.create_rectangle(x, y, x + parts_size, y + parts_size, fill=snake_color, tag="snake")
            self.squares.append(square)

class ObjectFood:

    def __init__(self):
        x = random.randint(0, int(screen_width / parts_size) - 1) * parts_size
        y = random.randint(0, int(screen_height / parts_size) - 1) * parts_size

        self.coords = [x, y]

        screen.create_oval(x, y, x + parts_size, y + parts_size, fill=food_color, tag="food")


def next_turn(snake, food):

    x, y = snake.coords[0]

    if direction == 'up':
        y -= parts_size
    elif direction == 'down':
        y += parts_size
    elif direction == 'left':
        x -= parts_size
    elif direction == 'right':
        x += parts_size

    snake.coords.insert(0, (x, y))

    square = screen.create_rectangle(x, y, x + parts_size, y + parts_size, fill=snake_color)

    snake.squares.insert(0, square)

    if x == food.coords[0] and y == food.coords[1]:

        global score
        screen.delete('food')
        food = ObjectFood()
        score += 1
        label.config(text='Score: {}'.format(score))

    else:
        del snake.coords[-1]

        screen.delete(snake.squares[-1])

        del snake.squares[-1]


    window.after(speed, next_turn, snake, food)

    if score == 25:
        screen.delete(ALL)
        screen.create_text(screen.winfo_width()/2, screen.winfo_height()/2, font=('consolas', 70), text='YOU WIN!\n 25 POINTS', fill="green")


def change_direction(snake_direction):

    global direction

    if snake_direction == 'left':
        if direction != 'right':
            direction = snake_direction
    elif snake_direction == 'right':
        if direction != 'left':
            direction = snake_direction
    elif snake_direction == 'up':
        if direction != 'down':
            direction = snake_direction
    elif snake_direction == 'down':
        if direction != 'up':
            direction = snake_direction


window = Tk()
window.title("Python Snake Game")
window.resizable(False, False)

direction_chooser = random.randint(1, 4)
direction = "down"

screen = Canvas(window, bg=bg_color, height=screen_height, width=screen_width)
screen.pack()

window.update()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = ObjectSnake()
food = ObjectFood()

next_turn(snake, food)

label = Label(window, text='Score: {}'.format(score), font=('consolas', 40))
label.pack()

window.mainloop()

# I'm not sure if this is the final one, but this is the only one I found.
