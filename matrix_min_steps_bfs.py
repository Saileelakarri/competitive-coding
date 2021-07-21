def findminsteps(mat,n,m):
    if mat[0][0]==0:
        return -1
    elif mat[0][0]==0:
        return 0
    queue=[]
    queue.append([0,0,0])
    while queue!=[]:
        pair=queue[0]
        #print(pair)
        i=pair[0]
        #print(i)
        j=pair[1]
        #print(j)
        steps=pair[2]
        #print(steps)
        queue.pop(0)
        if isvalid(i,j,mat):
            print("true",i,j)
            vmat[i][j]=1
            if isvalid(i-1,j,mat) and not(vmat[i-1][j]):
                if mat[i-1][j]==9:
                    return steps+1
                else:
                    queue.append([i-1,j,steps+1])
            if isvalid(i,j+1,mat) and not(vmat[i][j+1]):
                if mat[i][j+1]==9:
                    return steps+1
                else:
                    queue.append([i,j+1,steps+1])
            if isvalid(i+1,j,mat) and not(vmat[i+1][j]):
                if mat[i+1][j]==9:
                    return steps+1
                else:
                    queue.append([i+1,j,steps+1])
            if isvalid(i,j-1,mat) and not(vmat[i][j+1]):
                if mat[i][j-1]==9:
                    return steps+1
                else:
                    queue.append([i,j-1,steps+1])
                    
    return -1                

                
def isvalid(i,j,mat):
    if (i>=0 and i<n) and (j>=0 and i<m) and mat[i][j]!=0:
        return True
    return False
                
m,n=map(int,input().split())
mat=[]
vmat=[]
for i in range(m):
    l=list(map(int,input().split()))
    mat.append(l)
    l1=[0]*n
    vmat.append(l1)
#print(vmat)
#print(mat)
print(findminsteps(mat,n,m))    
