#Strong Number ==> ex:-145==>> 1! + 4! + 5! ==>1 + 24 + 120 ===> 145
def strongNum(num):
    sum=0
    num1=num
    while(num1!=0):
        temp=num1%10
        fact=1
        for i in range(1,temp+1):
            fact=fact*i
        sum=sum+fact
        num1=num1//10
    if sum==num:
        print(sum)
    else:
        print(False)
strongNum(145)
