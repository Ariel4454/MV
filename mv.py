import math
import turtle

# Ajusta las coordenadas del mundo para hacer la gráfica más pequeña
turtle.setworldcoordinates(-500, -500, 500, 500)

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(10000)
turtle.fillcolor("brown")

def draw_stem(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.fillcolor("green")  
    turtle.begin_fill()
    turtle.forward(350)  # Longitud del tallo aumenta
    turtle.left(90)
    turtle.forward(50)   # Ancho del tallo aumentado
    turtle.left(90)
    turtle.forward(350)
    turtle.end_fill()

# Dibuja un girasol
def draw_sunflower(x, y):
    # Dibuja el centro de la flor
    turtle.penup()
    turtle.goto(x, y + 180)
    turtle.fillcolor("#8B4513")  
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Dibuja los pétalos
    phi = 137.508 * (math.pi / 180.0)
    for i in range(60 + 40):
        r = 4 * math.sqrt(i)
        theta = i * phi
        petal_x = r * math.cos(theta) + x
        petal_y = r * math.sin(theta) + y + 180
        turtle.penup()
        turtle.goto(petal_x, petal_y)
        turtle.setheading(i * 137.508)
        turtle.pendown()
        if i < 60:
            turtle.stamp()
        else:
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.right(20)
            turtle.forward(70)
            turtle.left(40)
            turtle.forward(70)
            turtle.left(140)
            turtle.forward(70)
            turtle.left(40)
            turtle.forward(70)
            turtle.end_fill()

# Posición inicial del tallo
stem_x, stem_y = 0, -200

# Dibujar el tallo más largo y ancho
draw_stem(stem_x, stem_y)

# Dibujar cada girasol en las nuevas posiciones
positions = [(-400, -40), (-200, 80), (-200, -180), (0, 200), (0, 0), (200, 80), (200, -180), (400, -40)]
for position in positions:
    draw_sunflower(position[0], position[1])

# Ajustar la posición del texto para que esté más arriba
turtle.penup()
turtle.goto(0, 400)  
turtle.color("red") 
turtle.write("Feliz dia!!! Espero poder darte unas reales", align="center", font=("Arial", 24, "bold"))

turtle.hideturtle()
turtle.exitonclick()
