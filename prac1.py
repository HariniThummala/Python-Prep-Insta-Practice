'''
Input 1 :
1 10 4
Output 1 :
1+5+9+13+17+21+25+29+33+37=190
'''
x,y,z=map(int,input().split(' '))
s=0
for i in range(y):
    t=x+i*z
    s=s+t
    if i<y-1:
        print(t,end='+')
    else:
        print(t,end='=')
print(s)
    



    
    
