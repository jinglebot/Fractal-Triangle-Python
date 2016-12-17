import turtle

def draw_triangle(some_turtle, lt):
    for i in range (0, 3):
        some_turtle.forward(lt)
        some_turtle.left(120)

def draw_shape():

    #create screen
    windows = turtle.Screen()
    windows.bgcolor("lightblue")

    #create triangle jen
    jen = turtle.Turtle()
    jen.penup()
    jen.pensize(1)
    jen.shape("turtle")
    jen.color("blue", "purple")
    jen.speed(0)

    #create fractal triangle
    def draw_fractal(some_turtle, x, y, length, angle):
        if length <=10:
            return
        some_turtle.left(angle)
        some_turtle.goto(x, y)
        some_turtle.pendown()
        draw_triangle(some_turtle, length)
        some_turtle.penup()
        draw_fractal(some_turtle, x, y, length/2, angle)
        draw_fractal(some_turtle, length/2 + x, y, length/2, angle)
        draw_fractal(some_turtle, length/4 + x, ((length**2 - (length/2)**2)**(0.5))/2 + y, length/2, angle)
        return
        
    draw_fractal(jen, -200, -200, 500, 0)
    
    windows.exitonclick()

draw_shape()
