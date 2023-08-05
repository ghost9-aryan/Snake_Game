import tkinter as tk
import time as t
import pygame
import random
from tkinter import messagebox

def start_game():
    # define constants for the game
    WIDTH = 1475
    HEIGHT = 1000
    DOT_SIZE = 10
    MAX_RAND_POS = 70

    # initialize variables for the game
    score = 0
    delay = 100
    direction = 'Right'
    snake_positions = [(0, 0), (10, 0), (20, 0)]
    food_position = (0, 0)
    game_over = False

    # destroy the introduction window
    intro_window.destroy()

    # main window
    root = tk.Tk()
    root.state('zoomed')
    root.title("Snake Game")

    # canvas to display the game
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    # create a score label
    score_label = tk.Label(root, text="Score: {}".format(score))
    score_label.place(x=800, y=700)
    

    # exit button
    def exit_game():
        root.destroy()

    exit_button = tk.Button(root, text="Exit", command=exit_game, font=("Arial", 12))
    exit_button.place(x=700, y=700)

    # function to update the score label
    def update_score():
        nonlocal score
        score += 10
        score_label.config(text="Score: {}".format(score))
        

    # function to create a new food position
    def create_food():
        nonlocal food_position
        x = random.randint(0, MAX_RAND_POS) * DOT_SIZE
        y = random.randint(0, MAX_RAND_POS) * DOT_SIZE
        food_position = (x, y)
        canvas.create_oval(x, y, x + DOT_SIZE, y + DOT_SIZE, fill='red', tag='food')

    # function to move the snake
    def move_snake():
        nonlocal direction, game_over
        head_x, head_y = snake_positions[-1]

        # update position of snake's head
        if direction == 'Up':
            new_head = (head_x, head_y - DOT_SIZE)
        elif direction == 'Down':
            new_head = (head_x, head_y + DOT_SIZE)
        elif direction == 'Left':
            new_head = (head_x - DOT_SIZE, head_y)
        elif direction == 'Right':
            new_head = (head_x + DOT_SIZE, head_y)
        else:
            return

        # check if snake has collided.
        if new_head[0] >= WIDTH or new_head[1] >= HEIGHT or new_head[0] < 0 or new_head[1] < 0:
            print("GAME OVER!!!")
            print('')
            messagebox.showinfo("GAME OVER", 'Game Over !!')
            root.destroy()

        # check if snake has eaten food
        elif new_head == food_position:
            update_score()
            canvas.delete('food')
            create_food()

        else:
            snake_positions.pop(0)

        # add new head to snake's position
        snake_positions.append(new_head)

        # update snake's position on canvas
        canvas.delete('snake')
        for x, y in snake_positions:
            canvas.create_rectangle(x, y, x + DOT_SIZE, y + DOT_SIZE, fill='green', tag='snake')

        # update delay and call function again
        root.after(delay, move_snake)

    # function to change direction of snake
    def change_direction(new_direction):
        nonlocal direction
        if new_direction in ['Up', 'Down', 'Left', 'Right']:
            direction = new_direction

    # bind arrow keys to change_direction function
    root.bind('<Up>', lambda event: change_direction('Up'))
    root.bind('<Down>', lambda event: change_direction('Down'))
    root.bind('<Left>', lambda event: change_direction('Left'))
    root.bind('<Right>', lambda event: change_direction('Right'))

    # initialize game
    create_food()
    move_snake()

    root.mainloop()


# create the introduction window
intro_window = tk.Tk()
intro_window.title("Snake Game - Introduction")

# set the introduction window size to maximum
intro_window.state('zoomed')

# create a label for the introduction
intro_label = tk.Label(intro_window, text="Welcome to Snake Game!\n\nPress 'Start' to begin the game.",
                      font=("Arial", 32))
intro_label.place(x=400, y=100)

def game():
    start_game()

start_button = tk.Button(intro_window, text="Start", command=game, font=("Arial", 42), bg='red', fg='orange')
start_button.place(x=600, y=500)

# exit button
def exit_intro():
    intro_window.destroy()

exit_button = tk.Button(intro_window, text="Exit", command=exit_intro, font=("Arial", 12))
exit_button.place(x=1200, y=700)

pygame.mixer.init()  # initialize the pygame

def toggle_switch():
    if switch_var.get() == 1:
        # Switch is turned ON
        pygame.mixer.music.load("C:\\Users\\aryan\\Desktop\\bg.mp3")
        pygame.mixer.music.play(loops=-1)
    else:
        # Switch is turned OFF
        print("Switch is OFF")
        pygame.mixer.music.stop()  # Stop background music

# Variable to track the state of the switch
switch_var = tk.IntVar()

# Create the toggle switch
def toggle_button():
    toggle_switch()

toggle_button = tk.Checkbutton(intro_window, text="Music", variable=switch_var, command=toggle_switch, onvalue=1, offvalue=0,font=("Arial", 22))
toggle_button.place(x=100, y=600)

intro_window.mainloop()
