# Square Tester Class

from Shape import Square


class SquareTester():

    def main():
        s = Square('45', 'yellow')
        print(s) # test __repr__

        print("My side is " + str(s.getSide()) + " units.")
        print("My area is " + str(s.getArea()) + " units.")
        print("My perimeter is " + str(s.getPerimeter()) + " units.")

        print("My color is " + s.getColor())
        print("I will now change colors to forest green.")
        s.setColor('forest green')
        print("My color is now " + s.getColor())

        print("I descibe myslef as: " + s.describe())

    if __name__ == "__main__":
        main()