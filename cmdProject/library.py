
class Library:
    def __init__(self, blist, bname):
        self.bkList = blist
        self.bkName = bname
        self.store = {}
        
    print("Welcome to the {main_library.name} library.")
    print("1. Show Book List")
    print("2. Credit The Book")
    print("3. Add The Book")
    print("4. Return The Book")
    

if __name__ == "__main__":
    main_library = Library(["Himu somogro", "Python", "ML", "ML_Python", "7th havit of life"], "Imam Library's")
  