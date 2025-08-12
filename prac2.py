def fun(array,l):
    c=0
    for i in range(0,l):
        for j in range(i+1,l):
            if i<j and array[i]>array[j]:
                c+=1
    print(c)
array=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    array.append(x)
fun(array,n)
