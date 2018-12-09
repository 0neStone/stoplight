import turtle
import time

# Aufgabe: Ampel erstellen, die mit Bytes gesteuert wird

pen = turtle.Turtle()  # Initialize pen
pen.hideturtle()
pen.speed(100)

class Stoplight:
    def __init__(self, radius):
        self.r = radius
        self.width = 2*self.r +20
        self.height = 3*(2*self.r) +40

    # Create black box in which all the lights fit
    def create_box(self):
        pen.color("black", "black")

        pen.up()
        pen.goto(-(self.width/2), self.height/2)
        pen.down()

        pen.begin_fill()
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.end_fill()

        pen.left(90)

    # Rotes Licht erschaffen/verändern
    def red_light(self, byte: str):
        color = "grey"
        if byte == "00000011":
            color = "red"

        pen.up()
        pen.goto(0, -self.r)
        pen.down()
        pen.color("grey", color)
        pen.begin_fill()
        pen.circle(self.r)
        pen.end_fill()

    # Gelbes Licht erschaffen/verändern
    def yellow_light(self, byte: str):
        color = "grey"
        if byte == "00000010":
            color = "yellow"

        pen.up()
        pen.goto(0, self.r)
        pen.down()
        pen.color("grey", color)
        pen.begin_fill()
        pen.circle(self.r)
        pen.end_fill()

    # Grünes Licht erschaffen/verändern
    def green_light(self, byte: str):
        color = "grey"
        if byte == "00000001":
            color = "green"

        pen.up()
        pen.goto(0, 3*self.r)
        pen.down()
        pen.color("grey", color)
        pen.begin_fill()
        pen.circle(self.r)
        pen.end_fill()

    # Lichter zum ersten Mal erstellen
    def create_lights(self):
        self.create_box()
        self.green_light("00000001")
        self.yellow_light("00000010")
        self.red_light("00000011")

    # Lichter durch Byte-Befehle verändern
    def change_lights(self, byte: str):
        self.green_light(byte)
        self.yellow_light(byte)
        self.red_light(byte)

Light1 = Stoplight(80)

Light1.create_lights()
time.sleep(2)
Light1.change_lights("00000001") # green light
time.sleep(2)
Light1.change_lights("00000010") # yellow light
time.sleep(2)
Light1.change_lights("00000011") # red light

turtle.mainloop()
