#factorial of a number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
n=int(input())
fact(n)
        
