import turtle
import time

# Aufgabe: Ampel erstellen, die mit Bytes gesteuert wird

pen = turtle.Turtle()  # Initialize pen
pen.hideturtle()
pen.speed(100)
r: int = 80
width: int = 2*r +20
height: int = 3*(2*r) +40

# Create black box in which all the lights fit
def create_box():
    pen.color("black", "black")

    pen.up()
    pen.goto(-(width/2), height/2)
    pen.down()

    pen.begin_fill()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.end_fill()

    pen.left(90)

# Rotes Licht erschaffen/verändern
def red_light(byte: str):
    color = "grey"
    if byte == "00000011":
        color = "red"

    pen.up()
    pen.goto(0, -r)
    pen.down()
    pen.color("grey", color)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()

# Gelbes Licht erschaffen/verändern
def yellow_light(byte: str):
    color = "grey"
    if byte == "00000010":
        color = "yellow"

    pen.up()
    pen.goto(0, r)
    pen.down()
    pen.color("grey", color)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()

# Grünes Licht erschaffen/verändern
def green_light(byte: str):
    color = "grey"
    if byte == "00000001":
        color = "green"

    pen.up()
    pen.goto(0, 3*r)
    pen.down()
    pen.color("grey", color)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()

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

turtle.mainloop()
