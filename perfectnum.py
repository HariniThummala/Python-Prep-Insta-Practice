#perfect number 28
#factors of 28 are--> 1,2,4,7,14
# sum of all factors--> 1+2+4+7+14
#                   --> 28
# so its a perfect number
def isPer(num):
    sum=0
    n=num
    for i in range(1,int(n/2)+1):
        if num%i==0:
            sum=sum+i
        else:
            continue
    if sum==num:
        print(sum)
    else:
        print(False)
isPer(6)
