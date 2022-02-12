def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#n=int(input("Input a number to compute the factiorial : "))
n=8
print(factorial(n))