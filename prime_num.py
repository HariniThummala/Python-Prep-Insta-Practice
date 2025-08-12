#Prime Number program
def isPrime(num):
    if num<1:
        print("its a prime number")
    else:
        for i in range(2,int(num*(0.5))+1):
            if num%i==0:
                print("Its not a prime number")
                return
        print("Its a prime number")
n=int(input())
isPrime(n)
