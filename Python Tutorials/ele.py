#print n to 1 backwards
#recursive function
def show(n):
    if(n==0):
        return  #returns None
    print(n)
    show(n-1)

print(show(5))