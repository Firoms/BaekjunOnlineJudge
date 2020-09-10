
# import turtle as t
# side = 100
# angle = 90
# for j in range(4):
#     for i in range(4):
#         t.fd(side)
#         t.right(angle)
#     t.left(angle)

# import math
# a = int(input("반지름을 입력하세요:"))
# b = "%0.4f" % float(a*a*math.pi)
# print(f"반지름이 {a}인 원의 넓이 = {b}")


# import turtle as t
# radius = 50
# for i in range(3):
#     t.pendown()
#     t.circle(radius)
#     radius += 20
#     t.penup()
#     t.fd(100)


from turtle import *
import math
speed(10000)
color('white')
bgcolor('black')
penup()
goto(0, -200)
pendown()
min_length = 20


def draw_branch(l, w):
    left(15)
    draw_stick(l, w)
    right(30)
    draw_stick(l, w)
    left(15)


def draw_stick(l, w):
    width(w)
    forward(l)
    if min_length < l:
        draw_branch(math.ceil(l*0.8), math.ceil(w*0.6))
    backward(l)


penup()
setheading(90)
pendown()
draw_branch(100, 10)
