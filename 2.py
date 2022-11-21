s1,s2=map(str,input().split(', '))
s1=s1[1:-1]
s2=s2[1:-1]
c=s2[-1]

count=0
for i in s1:
    if(c==i):
        count+=1

print(count)
