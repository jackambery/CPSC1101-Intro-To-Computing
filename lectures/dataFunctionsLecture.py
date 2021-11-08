'''
data functions
- these are not really found in other languages

I understand it as a quick way of doing an operation on a whole list 
and returning that list, now calculated

'''
import math

def sq(num):
    print(math.sqrt(num))

def fun1():
    [ sq(x) for x in [8, 9, 10] ]

def fun2():
    # for every x in my list, do 2 * x
    lc = [ 2*x for x in [0, 1, 2, 3, 4, 5] ]
    print(lc)

def fun3():
    lc = [ 10 * x for x in [0, 1, 2, 3, 4, 5] if x % 2 == 0] # you can add a conditional to the iteration
    print(lc)

def fun4():
    lc = [ y * 21 for y in range(0, 3) ]
    print(lc)

# gets the second letter of each string in given list
def fun5():
    lc = [ s[1] for s in ["jack", "ambery"]]
    print(lc)

def main():
    fun1()
    fun2()
    fun3()
    fun4()
    fun5()

if __name__ == "__main__":
    main()