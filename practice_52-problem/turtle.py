import turtle

name = turtle.textinput("name", "What your name?")
name = name.lower()

if name.startswith("mr"):
    print("Hello Sir. how are you?")
    
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Medam. how are you?")
    
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)
    
turtle.exitonclick()