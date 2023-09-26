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

num = int(input("Enter a number: "))
print("Prime factors are: ", prime_factors(num))

satisfaction = input("Are you satisfied with the result? (yes/no): ")
if satisfaction.lower() == 'yes':
    print("Great! We're happy to help.")
else:
    print("We're sorry to hear that. We'll try to improve.")