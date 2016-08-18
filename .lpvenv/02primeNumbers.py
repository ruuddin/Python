
# Inefficient prime implementation
primes = []

upto = 100
for n in range(2, upto + 1):
    is_Prime = True

    for divisor in range(2, n):
        if n % divisor == 0:
            is_Prime = False
            break
    if is_Prime:
        primes.append(n)

print primes


# Efficient prime implementation
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else: # special else block which does not run if break statement is executed,
            # and runs if for loop finishes successfully
        primes.append(n)

print primes