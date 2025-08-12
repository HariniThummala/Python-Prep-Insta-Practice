#A Number that is divisible by the sum of it's digits is known as a Harshad number
# 21 ==> 2+1=3
#21 is divisible by 3
def harSHadNum(num):
    sum=0
    n=num
    while(n!=0):
        temp=n%10
        sum=sum+temp
        n=n//10
    if num%sum==0:
        print(True)
    else:
        print(False)
harSHadNum(35)
