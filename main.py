import random
import turtle as t
color_list = [(238, 236, 234), (34, 108, 167), (223, 229, 235), (245, 77, 36), (112, 163, 211), (153, 57, 85),
              (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152),
              (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192)
              ]
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
for i in range(10):
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)