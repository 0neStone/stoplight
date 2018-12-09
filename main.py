import turtle
import time

turtle.title("Johannes' Stoplight")

class Stoplight:
    def __init__(self, radius, x, y):
        self.r = radius
        self.x = x              # Verschiebung in y und x Richtung
        self.y = y
        self.width = 2*self.r +20
        self.height = 3*(2*self.r) +40

        self.pen = turtle.Turtle()  # Initialize pen
        self.pen.hideturtle()
        self.pen.speed(100)

    # Create black box in which all the lights fit
    def create_box(self):
        self.pen.color("black", "black")

        self.pen.up()
        self.pen.goto(-(self.width/2) + self.x, self.height/2 + self.y)
        self.pen.down()

        self.pen.begin_fill()
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.end_fill()

        self.pen.left(90)

    # Rotes Licht erschaffen/verändern
    def red_light(self, byte: str):
        color = "grey"
        if byte == "00000011":
            color = "red"

        self.pen.up()
        self.pen.goto(0 + self.x, -self.r + self.y)
        self.pen.down()
        self.pen.color("grey", color)
        self.pen.begin_fill()
        self.pen.circle(self.r)
        self.pen.end_fill()

    # Gelbes Licht erschaffen/verändern
    def yellow_light(self, byte: str):
        color = "grey"
        if byte == "00000010":
            color = "yellow"

        self.pen.up()
        self.pen.goto(0 + self.x, self.r + self.y)
        self.pen.down()
        self.pen.color("grey", color)
        self.pen.begin_fill()
        self.pen.circle(self.r)
        self.pen.end_fill()

    # Grünes Licht erschaffen/verändern
    def green_light(self, byte: str):
        color = "grey"
        if byte == "00000001":
            color = "green"

        self.pen.up()
        self.pen.goto(0 + self.x, 3*self.r + self.y)
        self.pen.down()
        self.pen.color("grey", color)
        self.pen.begin_fill()
        self.pen.circle(self.r)
        self.pen.end_fill()

    # Lichter zum ersten Mal erstellen
    def create_lights(self):
        self.red_light("00000011")

    # Lichter durch Byte-Befehle verändern
    def change_lights(self, byte: str):
        self.green_light(byte)
        self.yellow_light(byte)
        self.red_light(byte)

    def run_lights(self, repeat: int):
        time.sleep(2)
        for i in range(repeat):
            # Falls Benutzer das Programm schließt
            try:
                self.change_lights("00000001") # green light
                time.sleep(2)
                self.change_lights("00000010") # yellow light
                time.sleep(2)
                self.change_lights("00000011") # red light
                time.sleep(2)
                self.change_lights("00000010") # yellow light
                time.sleep(2)
            except:
                pass

Light1 = Stoplight(80, -200, 0)
Light1.create_lights()
Light2 = Stoplight(80, 200, 0)
Light2.create_lights()

Light1.run_lights(2)
Light2.run_lights(2)

turtle.mainloop()    self.create_box()
        self.green_light("00000001")
        self.yellow_light("00000010")
        self.red_light("00000011")

    # Lichter durch Byte-Befehle verändern
    def change_lights(self, byte: str):
        self.green_light(byte)
        self.yellow_light(byte)
        self.red_light(byte)

    def run_lights(self, repeat: int):
        time.sleep(2)
        for i in range(repeat):
            # Falls Benutzer das Programm schließt
            try:
                self.change_lights("00000001") # green light
                time.sleep(2)
                self.change_lights("00000010") # yellow light
                time.sleep(2)
                self.change_lights("00000011") # red light
                time.sleep(2)
                self.change_lights("00000010") # yellow light
                time.sleep(2)
            except:
                pass

Light1 = Stoplight(80, -200, 0)
Light1.create_lights()
Light2 = Stoplight(80, 200, 0)
Light2.create_lights()

Light1.run_lights(2)
Light2.run_lights(2)

turtle.mainloop()
