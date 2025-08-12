#Armstrong Number like 153==> 1^3+5^3+3^3 ==> 1+125+27 ==>153
def isArm(num):
    sum=0
    while(num!=0):
        temp=num%10
        sum=sum+(temp**3)
        num=num//10
    return sum
n=int(input())
res=isArm(n)
if res==n:
    print("Its an Armstrong number")
else:
    print("Its not an Armstrong number")
