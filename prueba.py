def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
        print("Iteration: ", i, "Factors so far: ", factors)  # Print each iteration and the factors found so far
    if n > 1:
        factors.append(n)
    return factors

name = input("Enter your name: ")
surname = input("Enter your surname: ")
num = int(input("Enter a number: "))
print("Prime factors are: ", prime_factors(num))