#find out factorial of N
def calc_fact(N):
    fact = 1
    for i in range(1,N + 1):
        fact *= i
    print(fact)

calc_fact(8)
calc_fact(100)

