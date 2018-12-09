from turtle import *
import time

# Aufgabe: Ampel erstellen, die mit Bytes gesteuert wird

t=Turtle(shape='classic')  #Turtle “t“ erstellen
t.hideturtle()
t.speed(100)
r: int = 80
width: int = 2*r +20
height: int = 3*(2*r) +40

# Create black box in which all the lights fit
def create_box():
    t.color("black", "black")

    t.up()
    t.goto(-(width/2), height/2)
    t.down()

    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.end_fill()

    t.left(90)

# Rotes Licht erschaffen/verändern
def red_light(byte: str):
    color = "grey"
    if byte == "00000011":
        color = "red"

    t.up()
    t.goto(0, -r)
    t.down()
    t.color("grey", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# Gelbes Licht erschaffen/verändern
def yellow_light(byte: str):
    color = "grey"
    if byte == "00000010":
        color = "yellow"

    t.up()
    t.goto(0, r)
    t.down()
    t.color("grey", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# Grünes Licht erschaffen/verändern
def green_light(byte: str):
    color = "grey"
    if byte == "00000001":
        color = "green"

    t.up()
    t.goto(0, 3*r)
    t.down()
    t.color("grey", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# Lichter zum ersten Mal erstellen
def create_lights():
    create_box()
    green_light("00000001")
    yellow_light("00000010")
    red_light("00000011")

# Lichter durch Byte-Befehle verändern
def change_lights(byte: str):
    green_light(byte)
    yellow_light(byte)
    red_light(byte)

create_lights()
time.sleep(2)
change_lights("00000001") # green light
time.sleep(2)
change_lights("00000010") # yellow light
time.sleep(2)
change_lights("00000011") # red light

mainloop()
