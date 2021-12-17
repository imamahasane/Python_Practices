"""
Lets say you are running a 5 km race. Write a program that,
   1. Upon completing each 1 km asks you "are you tired?"
   2. If you reply "yes" then it should break and print "you didn't finish the race"
   3. If you reply "no" then it should continue and ask "are you tired" on every km
   4. If you finish all 5 km then it should print congratulations message
"""

for i in range(5):
    print(f"you ran {i + 1} km.")
    ans = input("are you tired? (yes/no): ")

    if ans == 'yes':
        break

if i == 4:
    print(f"congratulations you run {i+1} km.")

else:
    print(f"You didn't finish the race.")