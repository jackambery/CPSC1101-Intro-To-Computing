# Lab 7 Test Class

from Animal import Cat

def main():
    cat1 = Cat("Mittens", "Calico", "Meowwww", True)
    cat2 = Cat("Fluffy", "Persian", "Meeeeeow", False)

    print(cat1)
    print(cat2)

    print("Cat1 likes milk:", cat1.likesMilk())
    print("Cat2 likes milk:", cat2.likesMilk())

    cat1.updateMeow("MEOWW")
    print("Cat1 has changed meow sound.")
    print(cat1)

if __name__ == "__main__":
    main()