#program to find fibonacci series

def Fibonacci(n):
    if n==0:
        
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
#program starts here
print("program written by Sanjana BM 4SN21IS023")
n=int(input("enter a value"))
if n<0:

    print("invalid number")
print("fibonacci series of ",n,"is")
for i in range(n):
    print(Fibonacci(i))
