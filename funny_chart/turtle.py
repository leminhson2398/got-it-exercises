#
#   Requirement:
#       python version: 3.x
#   Run:
#       python assignment.py
#       

from turtle import Turtle, Screen
from typing import List


screen = Screen()

TURTLE_SIZE = 20
START_X, START_Y = TURTLE_SIZE/2 - screen.window_width()/2, TURTLE_SIZE/2 - \
    screen.window_height()/2
BAR_WIDTH = 60
NUM_OF_COLUMNS = 10
BG_COLORS = ["yellow", "navy", "red", "orange", "green", "blue", "skyblue", "purple", "black", "pink"]


def process_input() -> List[int]:

    data_list: List[int] = []

    print(".........Welcome to chart drawing...........")
    
    while NUM_OF_COLUMNS != len(data_list):
        data = input(f"Enter data {len(data_list) + 1}: ")
        data = data.strip()

        try:
            float_data = float(data)
        except ValueError:
            print("Please enter real number.")
        else:
            rounded_data = round(float_data)
            data_list.append(rounded_data)

    print("Good job!")
    return data_list


def app() -> None:

    int_list = process_input()
    print("Drawing chart, take a look at the window.")

    cursor = Turtle()
    cursor.penup()
    cursor.goto(START_X, START_Y)
    cursor.pendown()
    cursor.right(90)
    cursor.showturtle()

    for index in range(len(int_list)):
        data = int_list[index]
        color = BG_COLORS[index % len(BG_COLORS)]

        cursor.fillcolor(color)
        cursor.begin_fill()

        cursor.left(180)
        cursor.forward(data)
        cursor.write(f"{data}")
        cursor.right(90)
        cursor.forward(BAR_WIDTH)
        cursor.right(90)
        cursor.forward(data)

        cursor.end_fill()

    
    screen.mainloop()


if __name__ == "__main__":
    app()
