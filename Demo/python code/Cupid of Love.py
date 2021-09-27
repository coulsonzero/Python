from turtle import *
import turtle
from tkinter import *
import subprocess
import os
import random as ran


def Circlemove(size):
    for i in range(200):
        right(1)
        forward(1 * size)


def Heart(x, y, size):
    setturtle(x, y)
    speed(0.6)
    color('red', 'pink')
    begin_fill()
    left(140)
    forward(111.65 * size)
    Circlemove(size)
    left(120)
    Circlemove(size)
    forward(111.65 * size)
    end_fill()
    penup()


def setturtle(x, y):
    penup()
    goto(x, y)
    pendown()


def Line():
    speed(0.6)
    pensize(10)
    setheading(0)
    setturtle(-300, 0)
    left(12)
    forward(210)
    setturtle(80, 80)
    forward(150)


def LineHead():
    pensize(1)
    speed(0.5)
    color('red', 'red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()


def SavePicture():
    ts = getscreen()
    ts.getcanvas().postscript(file="520.ps", colormode='color')
    window = turtle.Screen()
    window.exitonclick()


def main():
    Love_Words = ["    滨冰，七夕快乐！"]
    Love_Letter = ["有你陪伴的日子，真好。", "遇见你，此生甚幸。"]
    Random_Number = ran.randint(0, len(Love_Words) - 1)
    setup(800, 600, 0, 0)
    getscreen().tracer(30, 0)
    hideturtle()
    pensize(3)
    color('red', 'pink')
    Heart(0, -25, 0.75)
    home()
    Heart(-80, -50, 1)
    Line()
    LineHead()
    pencolor("black")
    speed(0.6)
    j = 0
    for i in Love_Words[Random_Number]:
        j = j + 1
        setturtle(j * 25 - 250, -150 + ran.randint(-1, 1) * 7)
        write(i, font=("华文行楷", 25, "normal"))
    j = 0
    pencolor("gold")
    for i in Love_Letter:
        j = j + 1
        setturtle(-400, 275 - j * 27)
        write(i, font=("华文行楷", 25, "normal"))
    pencolor('black')
    SavePicture()


if __name__ == '__main__':
    main()
