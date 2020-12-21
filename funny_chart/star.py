
#
#   Requirement:
#       python version: 3.x
#   Run:
#       python assignment.py
#       

from turtle import Turtle, Screen, TurtleGraphicsError
from typing import List
import random


screen = Screen()

NUM_OF_COLORS = 5
NUM_OF_STARS = 7
DEFAULT_COLOR = "black"
STAR_SIZE_RANGE = [30, 200]
START_POS_RANGE = [-200, 200]

cursor = Turtle()
cursor.shape("turtle")


def process_input() -> List[int]:

    data_list: List[int] = []

    print(".........Welcome to star drawing...........")
    
    while NUM_OF_COLORS != len(data_list):
        data = input(f"Enter data {len(data_list) + 1}: ")
        data = data.strip()
        data_list.append(data)

    print("Good job!")
    return data_list

def stammo(x: int, y: int, length: int, color: str) -> None:

    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()

    try:
        cursor.pencolor(color)
        cursor.fillcolor(color)
    except TurtleGraphicsError:
        print(f"{color} is not a color name. Changing to default")
        cursor.pencolor(DEFAULT_COLOR)
        cursor.fillcolor(DEFAULT_COLOR)    

    cursor.begin_fill()
    for i in range(5):
        cursor.forward(length)
        cursor.right(144)

    cursor.end_fill()
    cursor.penup()

def app() -> None:

    clist = process_input()
    print("Drawing stars, take a look at the window.")
    cursor.showturtle()

    for index in range(NUM_OF_STARS):
        color = random.choice(clist)
        star_size = random.randrange(*STAR_SIZE_RANGE)
        star_pos_x = random.randrange(*START_POS_RANGE)
        star_pos_y = random.randrange(*START_POS_RANGE)

        stammo(star_pos_x, star_pos_y, star_size, color)

    
    screen.mainloop()


if __name__ == "__main__":
    app()
