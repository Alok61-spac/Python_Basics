# Find out the power of numbers
def power(N,n):
# Base Case
    if n == 0:
        return 1
# Recursive Case
    return N * power(N,n - 1)

N =int(input("Enter Your Base :"))
n = int(input("Enter your Exponent :"))
print("Result :" ,power(N,n))

