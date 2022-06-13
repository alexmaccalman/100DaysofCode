from os import stat
from tkinter import Y
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pd.read_csv("50_states.csv")
states = states_data.state.to_list()
TITLE = "Guess the State"
NUM_CORRECT = 0
guessed_states = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=TITLE, prompt="What's another state's name?")
    answer_state = answer_state.title()
    # check if the guess is among the 50 states
    if answer_state == "Exit":
        game_is_on = False
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = states_data[states_data.state == answer_state]
        # write correct guesses onto the map
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())
        guessed_states.append(answer_state)
        NUM_CORRECT += 1
        TITLE = f"{NUM_CORRECT}/50 Correct"

    if NUM_CORRECT == 50:
        game_is_on = False





