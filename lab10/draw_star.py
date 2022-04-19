'''
Yiming Ge
CS 5001, Fall 2021
Lab10

This is a program that
use turtle to draw the colorful star
'''

# import turtle
import turtle

# set pen
pen = turtle.Turtle()
pen.hideturtle()
# decide colors
cir = ['sienna', 'yellow', 'lime', 'blue', 'goldenrod']

# Draw one star pattern first


def draw_star(a_turtle, length, color):
    SIDES = 5
    a_turtle.pendown()
    for side in range(SIDES):
        a_turtle.pencolor(color[side])
        a_turtle.forward(length)
        a_turtle.right(2 * 360 / SIDES)
    a_turtle.penup()

# Draw all the stars together


def draw_all_stars(a_turt, length, edges, edge_increase):
    SIDES = 5
    a_turt.pendown()
    for i in range(edges):
        col = cir[i % 5]
        a_turt.color(col)
        a_turt.forward(length)
        length += edge_increase
        a_turt.right(2 * 360 / SIDES)
    a_turt.penup()


def main():
    ###### Solution one: draw one star then draw others ######
    # STAR_NUM = 4
    # length = 100
    # # set pen size
    # pen.pensize(3)
    # # then draw other stars
    # for i in range(STAR_NUM):
    #     draw_star(pen, length, cir)
    #     length = length + 100
    #     pen.penup()
    #     pen.goto(pen.xcor() - 50, pen.ycor() + 20)
    #     pen.pendown()

    # for i in range(2):
    #     draw_star(pen, length, cir)
    #     length = length + 100
    #     pen.penup()
    #     pen.goto(pen.xcor() - 50, pen.ycor() + 15)
    #     pen.pendown()

    ####### Solution two: draw all the stars together ######
    pen.pensize(3)
    length = 100
    edges = 20  # 4 * 5
    edge_increase = 30
    draw_all_stars(pen, length, edges, edge_increase)
    turtle.done()


if __name__ == "__main__":
    main()
