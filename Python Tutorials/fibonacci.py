#recursive function to find fibonacci sequence of first n numbers
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2)+fib(n-1)
n=int(input("enter a number:"))#positive numbers
if n<0: #negative numbers
    print("Number is not valid")

i=0
for i in range(0,n+1):
    print(fib(i))
