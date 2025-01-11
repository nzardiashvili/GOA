import turtle
def draw_triangle():
    for _ in range(3):
        turtle.forward(50)
        turtle.left(120)

def draw_triangles():
    for i in range(1, 121):
        if i % 2 == 1:
            turtle.color("green")
        else:
            turtle.color("blue")
        draw_triangle()
        turtle.forward(60)
        turtle.speed
        draw_triangles()
        turtle.done()

