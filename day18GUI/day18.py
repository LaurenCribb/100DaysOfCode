import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("deeppink1")

# DRAW A SQUARE
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# DRAW A DOTTED LINE
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# DRAW DIFFERENT SHAPES
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_shape(num_sides):
#     for degree in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
#     tim.color(random.choice(colours))


# for sides in range(3, 11):
#     draw_shape(sides)

# DRAW RANDOM WALK
# number_of_steps = random.choice(range(1, 100))
# tim.pensize(10)
# tim.speed(11)
# for _ in range(500):
#     direction = random.choice([0, 90, 180, 270])
#     tim.setheading(direction)
#     tim.forward(20)
#     tim.color(random.choice(colours))

# DRAW A SPIROGRAPH
turtle.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_colour = (red, green, blue)
    return random_colour


tim.speed(12)
# for _ in range(45):
#     tim.circle(100, 360)
#     tim.left(8)
#     tim.color(random_color())

# DAMIAN HIRST PAINTING
painting_colours = [(164, 169, 38), (140, 48, 106), (244, 79, 57), (3, 144, 60), (241, 66, 140), (249, 220, 224), (2, 142, 185), (162, 55, 52), (242, 102, 162),
                    (53, 203, 226), (211, 232, 234), (251, 228, 16), (22, 166, 128), (219, 237, 231), (253, 230, 0), (27, 195, 219), (156, 186, 168), (236, 164, 192)]
tim.penup()
tim.setpos(-200, -200)
for _ in range(10):
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(painting_colours))
        y = tim.pos()[1] + 50
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.goto(-200, y)

screen = turtle.Screen()
screen.exitonclick()
