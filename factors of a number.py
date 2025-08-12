# factor of a number
def factors(num):
    for i in range(2,num):
        if num%i==0:
            print(i)
factors(10)
