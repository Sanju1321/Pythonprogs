#function to print elements of a list in one line
def print_list(list,idx):
    if(idx==len(list)):
        return
    for i in range(0,idx+1):
     print(list[i],end=" ")
     i+=1
#example
list2=[2,3,7.8,"Hello"]     
n=print_list(list2,3)