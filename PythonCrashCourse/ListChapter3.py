motorxyxles = ["honda", "yamaha", "suzuki"]
print(motorxyxles)

motorxyxles3 = ["honda", "yamaha", "suzuki"]
motorxyxles3[0] = "ducati"
print(motorxyxles3)

motorxyxles2 = ["honda", "yamaha", "suzuki"]
motorxyxles2.append("ducati")
print(motorxyxles2)

motorxyxles4 = ["honda", "yamaha", "suzuki"]
motorxyxles4.insert(0, "ducati")
print(motorxyxles4)

motorxyxles5 = ["honda", "yamaha", "suzuki"]
motorxyxles5.insert(2, "ducati")
print(motorxyxles5)

motorxyxles6 = ["honda", "yamaha", "suzuki"]
del motorxyxles6[0]
print(motorxyxles6)

motorxyxles7 = ["honda", "yamaha", "suzuki"]
motorxyxles7.pop()
print(motorxyxles7)

motorxyxles8 = ["honda", "yamaha", "suzuki"]
motorxyxles8.pop(1)
print(motorxyxles8)

motorxyxles9 = ["honda", "yamaha", "suzuki"]
my_pop = motorxyxles9.pop(2)
print(f"MY new Motorcycles is {my_pop.title()}")

motorxyxles11 = ["honda", "yamaha", "suzuki"]
motorxyxles11.remove("honda")
print(motorxyxles11)
