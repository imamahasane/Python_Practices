import turtle

def bahu(s_lean):
    for i in range(4):
        turtle.forward(s_lean)
        turtle.left(90)
        
print(bahu(70))

turtle.exitonclick()