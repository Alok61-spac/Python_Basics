# Find out factorial of numbers
def fact(N):
    if( N == 0 or N == 1):
        return 1
    return N * fact(N - 1)
N =int(input("Enter Your Digit :"))
print(fact(N))



