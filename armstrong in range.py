def armR(num,m):
    for i in range(num,m+1):
        sum=0
        n1=i
        c=0
        while(n1!=0):
            t=n1%10
            c=c+1
            n1=n1//10
        n2=i
        while(n2!=0):
            temp=n2%10
            sum=sum+(temp**c)
            n2=n2//10
        if(sum==i):
            print(i)
        else:
            continue
armR(1,1000)
     
        
