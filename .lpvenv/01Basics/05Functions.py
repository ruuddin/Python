def f1():
    pass # no code needs to be executed, an empty function

#Ex1: Return tuple
print "Ex1"
def divmod(x, y):
    return x//y, x % y

print "\t", divmod(20, 7)

#Ex2: lambda/anonymous functions
print "Ex2"
def get_multiples_of_five(n):
    #Print list of all numbers up to n which are multiples of five.
    #filter - takes a lambda and an iterable, and returns an iterable
    return list(filter(lambda k: not k % 5, range(n)))

print "\t", get_multiples_of_five(50)

#Ex3: print function attributes
print "Ex3: "
def f3(a, b=1):
    return a * b
special_attributes = [
    "__doc__", "__name__", "__module__", "__defaults__", "__code__", "__globals__",
    "__dict__", "__closure__", #can end with a comma
]

for attr in special_attributes:
    print "\t", attr, '->', getattr(f3, attr)

#Ex4: get prime numbers in a range
#Algorithm rules
# prime of a number n is less than sqrt(n)
# dont need to check the division of all numbers upto sqrt(n), just check the division with prime.

from math import sqrt, ceil

print "Ex4"
def getPrimes(n):
    primes = []
    for candidate in range(2, n+1):
        isPrime = True
        root = int(ceil(sqrt(candidate)))
        for p in primes:
            if p > root:
                break
            if candidate % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(candidate)
    
    print "\t" ,primes

getPrimes(100)
