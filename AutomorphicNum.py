#Auto Morphic number
# 5*5 --> 25
#25 ends with 5 so 5 is an auto morphic num
def autoNum(num):
    ct=0
    n=num
    while (n!=0):
        ct=ct+1
        n=n//10
    print(ct)
    sqnum=num*num
    x=1
    for i in range(1,ct+1):
        x=x*10
    temp=sqnum%x
    if temp==num:
        print(True)
    else:
        print(False)
autoNum(76)

