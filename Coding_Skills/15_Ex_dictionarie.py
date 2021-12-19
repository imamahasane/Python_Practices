population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country = input("Enter country name to add: ")
    country = country.lower()

    if country in population:
        print("Country already exist in our dataset.")
        return

    p = input(f"Enter population for {country}: ")
    p = float(p)
    population[country] = p 
    print_all()

def remove():
    country = input("Enter country name to remove: ")
    country = country.lower()

    if country not in population:
        print("Country doesn't exist in our dataset.")
        return

    del population[country]
    print_all()

def query():
    country = input("Enter country name to query: ")
    country = country.lower()

    if country not in population:
        print("Country doesn't exist in our dataset.")
        return

    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country} - {p}")

def main():
    user_input = input("Enter operation (add, remove, query or print):")

    if user_input.lower() == 'add':
        add()

    elif user_input.lower() == 'remove':
        remove()

    elif user_input.lower() == 'query':
        query()

    elif user_input.lower() == 'print':
        print_all()


if __name__ == '__main__':
    main()

