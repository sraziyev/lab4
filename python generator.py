N = int(input("Squares.Input N: "))
sqrgenerator = (i ** 2 for i in range(1, N + 1))
for sqr in sqrgenerator:
    print(sqr)

n = int(input("Even numbers.Input n: "))
evens = (str(i) for i in range(0, n + 1) if i % 2 == 0)
print(", ".join(evens))

n = int(input("3 and 4 divisors.Input n: "))
thrfr = (str(i) for i in range(0, n + 1) if i % 3 == 0 and i % 4 == 0)
print(", ".join(thrfr))

a = int(input("Input starting number: "))
b = int(input("Input ending number: "))
squares = (i ** 2 for i in range(a, b + 1))
for sq in squares:
    print(sq)

n=int(input("Start from: "))
desc=(str(i) for i in range (n, -1, -1))
print(", ".join(desc))