# hw8
# CS 101: Homework #8
# Filename: hw8.py
# Date: 10 November 2021
#
# Name: John (Jack) Ambery
#
# A set of small problems to practive list comprehension

#q1
def q1():
    # squares each number from 0 to 4
    a = [ n**2 for n in range(0,5) ]
    print(a)

    # changes each value in given list to 42
    b = [ 42 for z in [0,1,2] ]
    print(b)

    # prints each number in list not changing them
    c = [ z for z in [0,1,2] ]
    print(c)

    # prints every other character in each string in list
    d = [ s[1::2] for s in ['aces','451!'] ]
    print(d)

    # multiplies each number in list by -7 only if they are greater than 4
    e = [ -7*b for b in range(-6,6) if abs(b)>4 ]
    print(e)

    # mulitplies each odd number in the set by itself minus 1
    f = [ a*(a-1) for a in range(8) if a%2==1 ]
    print(f)

#q2
def countas(s): # s is a string
    count = 0
    result = [1 for c in s if c == 'a']
    return sum(result)

#q3
def nodds(L): #L is a list of numbers
    LC = [1 for x in L if x % 2 == 1]
    return sum(LC)

#q4
def lotto(Y, W): # Y are my nums, W are the winning nums
    LC = [x for x in Y if W.count(x) >= 1]
    return len(LC)

#q5
def ndivs(N): # N is an int >= 2
    LC = [x for x in range(1, N + 1) if N % x == 0]
    return len(LC)

#q6
def primesUpTo(P): # P is an int >= 2
    LC = [ x for x in range(2, P + 1) if [y for y in range(2, x) if x % y == 0] == [] ]
    return LC

def main():
    q1()
    print("Number of a's:", countas('abcabbbacadeafrr'))
    print("Number of odds:", nodds([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]))
    lottoNums = lotto([1, 2, 3, 5, 6, 33], [33, 4, 99, 5])
    print("Matching numbers:", lottoNums)
    print("Number of divisors in 100:", ndivs(100))
    print("Primes up to 31:", primesUpTo(31))

if __name__ == "__main__":
    main()
