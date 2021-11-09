prompt = "\nTell me something Please."
prompt += "\n(Enter 'q' to the end program.) : "

active = True

while active:
    message = input(prompt)

    if message == "q":
        active = False

    else:
        print(message)

print("Copyright @ songkolok")
