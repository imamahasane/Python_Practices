def calculate_area(base, height):
    print(f"__name__ = {__name__}")
    return 1/2 * (base * height)


if __name__ == "__main__":
    print("I am in area.py")
    a = calculate_area(11, 22)
    print(f"Area: {a}")