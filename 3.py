def check(i):
    for j in i:
        if(j=='3' or j=='4' or j=='7'):
            return False
    return True


n=int(input())
i=1
while(1):
    if(check(str(i))):
        n-=1
        if(n==0):
            print(i)
            break
    i+=1
