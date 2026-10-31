import math
import turtle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

def heart_point(angle, size=1):
    x = 15 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )
    return x * size, y * size


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("#f73487")
pen.pensize(3)

points = 600
scale = 20
for i in range(points + 1):
    position = heart_point(2 * math.pi * i / points, scale)
    if i == 0:
        pen.penup()
        pen.goto(position)
        pen.pendown()
    else:
        pen.goto(position)

shape_points = [
    (x / 15, (y - 1) / 15)
    for x, y in (heart_point(2 * math.pi * i / 60) for i in range(60))
]
screen.register_shape("tiny_heart", shape_points)

heart_colors = ("#ff8ab5", "#ff4f91", "#ffc0d9", "#f73487", "#ff6fa5")
hearts = []
heart_count = 10
for i in range(heart_count):
    sprite = turtle.Turtle()
    sprite.shape("tiny_heart")
    sprite.color(heart_colors[i % len(heart_colors)])
    sprite.shapesize(stretch_wid=0.48, stretch_len=0.48)
    sprite.penup()
    hearts.append((sprite, i * 2 * math.pi / heart_count, 0.24 + (i % 5) * 0.085))

frame = 0


def animate():
    global frame
    frame += 1
    for sprite, offset, size in hearts:
        angle = offset + frame * 0.035
        sprite.goto(heart_point(angle, scale * size))
    screen.update()
    screen.ontimer(animate, 20)


screen.update()
animate()
turtle.done()
