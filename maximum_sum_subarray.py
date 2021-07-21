arr=list(map(int,input().split()))
sarr=[]
sarr.append(arr[0])
counter=1
for i in range(1,len(arr)):
    cur_sum=sarr[i-1]+arr[i]
    if cur_sum>=sarr[i-1]:
        counter+=1
        sarr.append(cur_sum)
    else:
        sarr.append(sarr[i-1])
print(max(sarr),counter)        
