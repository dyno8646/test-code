n=256
l=[]
for i in range(n):
    temp=list(map(int,input().split()))
    l.append(temp)
check=0
for i in range(n):
    for j in range(n):
        if(l[i][j]==0):
            check=1
            r1=i
            r2=i
            c1=j
            c2=j
            break
    if(check==1):
        break


for i in range(n):
    if(0 in l[i]):
        r2=i
        for j in range(len(l[i])):
            if(l[i][j]==0):
                if(j<=c1):
                    c1=j
                if(j>=c2):
                    c2=j


print((r1,c1),",",(r1,c2),",",(r2,c1),",",(r2,c2))
