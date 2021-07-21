n=int(input())
lst=list(map(int,input().split()))#1 2 3 4 5 5
ssum=sum(lst)
prev=lst[-1]
for i in range(n-2,-1,-1):
    if lst[i]!=prev:
        sl=lst[i]
        break
ssum2=n*sl
if ssum2>ssum:
    print(sl)
else:
    print(prev)
