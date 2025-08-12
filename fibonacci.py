#Fibonacci Sereis 0,1....
def fib(n):
    f0=0
    f1=1
    print(f0)
    print(f1)
    for i in range(0,n-1):
        f2=f0+f1
        f0=f1
        f1=f2
        print(f2)
n=int(input())
fib(n)
        
        
