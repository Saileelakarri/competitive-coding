def bfs(arr,n,start,end):
    queue=[]#taking queue
    l=[start,0]
    queue.append(l)#insert a pair (start,number of steps)
    vlist=[]#array to check if the particular node is visited or not
    vlist.append(queue[0][0])
    while queue!=[]:
        pair=queue[0]
        num=pair[0]
        steps=pair[1]#no.of steps
        queue.pop(0)#deleting front
        for i in arr:
            res=(num*i)%100000
            if res==end:
                steps+=1
                return steps
            if res not in vlist:
                vlist.append(res)
                l=[res,steps+1]
                queue.append(l)
    return -1        
start,end=map(int,input().split())    
arr=list(map(int,input().split()))
n=len(arr)
print(bfs(arr,n,start,end))
