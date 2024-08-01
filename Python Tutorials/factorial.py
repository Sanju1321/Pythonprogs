#recursive function to find the factorial of a given number
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

#example
p=fact(6)
print(p)