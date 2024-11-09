#Name: Jayden 
#Date: 11/09/2024 
#Description: This program will draw two different unique triangles 


import turtle

def start(tr, forward_user, color_user): 
  tr = turtle.Turtle() 
  
  tr.penup() 
  tr.forward(forward_user) 
  tr.pendown() 
  tr.color(color_user) 
                     
def triangle(tr, len): 
  if len > 10:
    for i in range(3):
      tr.forward(len)
      tr.left(120)
    return triangle(tr, len/2) 

def nestedTriange(tr, len):
  if len > 10:
    for i in range(3): 
      tr.forward(len)
      tr.left(120)
      return nestedTriangle(tr, len/2) 


def main():
  n = input("Enter a length") 
  tom = turtle.Turtle()
  start(tom, -100, "steelblue") 
  nestedTriangle(tom, n) 

  tess = turtle.Turtle() 
  start(tess, 100, "steelblue") 
  nestedTriangle(tess, n) 

if __name__ == "__main__":
  main() 

