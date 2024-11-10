#Name: Jayden 
#Date: 11/09/2024 
#Description: This program will draw two different unique triangles 
#CSci 127 Teaching Staff
#February 2018
#A template for a program that draws nested triangles 
#Modified by:  ADD YOUR NAME HERE

import turtle
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def triangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2).
    """
    if length > 10:
      for i in range(3):
        t.forward(length)
        t.left(120)
    return triangle(tr, length/2)    


def nestedTriangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2).
    """

     if length > 10:
       for i in range(3): 
         t.forward(length)
         t.left(120)
         return nestedTriangle(tr, length/2)       


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    triangle(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedTriangle(tess, n)

if __name__ == "__main__":
     main()


