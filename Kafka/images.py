from pathlib import Path
import random
import turtle
import time
directory=Path('./images')

file_paths=[str(file) for file in directory.rglob('*') if file.is_file()]


def random_image():
    image=random.choice(file_paths)
    screen=turtle.Screen()
    screen.addshape(image)
    jump_scare=turtle.Turtle()
    jump_scare.penup()
    jump_scare.shape(image)
    screen.update()
    time.sleep(0.1)
    jump_scare.hideturtle()
    screen.update()
    

        
print(random_image())