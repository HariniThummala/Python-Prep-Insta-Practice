#perfect square is 4==>2*2 9==> 3*3  but 6==>2*3 so its not a perfect num
def isPerNum(num):
    for i in range(1,int(num/2)+1):
        flag=1
        if i*i != num:
            flag=0
            continue
        else:
            break
    if flag==1:
        print(True)
    else:
        print(False)
isPerNum(9)
        
