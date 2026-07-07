#print numbers use recursion
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)

# Examples
show(68)
show(5)
show(61)