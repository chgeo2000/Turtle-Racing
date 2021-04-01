import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'cyan', 'yellow', 'black', 'purple', 'pink']


def get_number_of_racers():
    """
    This function asks the user for the number of racers
    :return: int, number of racers
    """
    while True:
        number_of_racers = int(input("Give the number of racers (2-8): "))
        if 2 <= number_of_racers <= 8:
            return number_of_racers
        else:
            print("Number of racers is not in range: 2-8... Try again!")


def init_screen():
    """
    This function initialise the screen (racetrack).
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


def create_racer(colors):
    """
    Creates racers and add them to a list
    :param colors: list, a list of colors
    :return: list, a list containing the racers
    """
    racers = []
    spacing_between_racers = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos((-WIDTH // 2) + (i + 1) * spacing_between_racers, -HEIGHT // 2 + 20)
        racer.pendown()
        racers.append(racer)
    return racers


def start_race(colors):
    """
    Simulates the actual race.
    :param colors: list, a list containing the colors of the participants
    :return: string, the color of the winning racer
    """
    racers = create_racer(colors)
    while True:

        for racer in racers:

            distance = random.randint(1, 15)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[racers.index(racer)]


random.shuffle(COLORS)
colors = COLORS[:get_number_of_racers()]  # number of colors = number of racers
init_screen()

print(f"The winner is the turtle with color: {start_race(colors)}!")
time.sleep(5)  # helps the user to see better who won
