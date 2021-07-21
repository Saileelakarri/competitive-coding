def main():
    t=int(input())
    l=[]
    for i in range(t):
        l1=list(map(int,input().split(" ")))
        l.append(l1)
    maxi=max([i[1] for i in l])
    mini=min([i[0] for i in l])
    lst=generateseive(mini,maxi)         
    for i in l:
        ll=i[0]
        rl=i[1]
        lst1=lst[ll:rl+1]
        le=list(x for x in lst1 if x!=0)
        if len(le)==1:
          print(0)
        elif len(le)==0:
          print(-1)
        else:
          print(max(le)-min(le))
          
def generateseive(mini,maxi):
    lst=[i for i in range(mini,maxi)]
    if 1 in lst:
        
        lst[1]=0
    for i in range(mini,maxi):
        for k in range(i+1,maxi+1):
            if k%i==0:
                lst[k]=0
    return lst            
             
main()

