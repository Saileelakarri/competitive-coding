t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=list(s)
    print(l)
    length=l.count('1')
    sarr=length*(length+1)//2
    print(sarr)
