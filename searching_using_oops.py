class Sorting:
    def __init__(self,data):
        self.data=data
    def selection_sort(self):
        pas=0
        for i in range(len(self.data)-1,-1,-1):
            pas+=1
            me=i
            for j in range(i-1,-1,-1):
                if(self.data[me]<self.data[j]):
                    me=j
            temp=self.data[me]
            self.data[me]=self.data[i]
            self.data[i]=temp
            #print(pas,"-->",self.data)
        #print(self.data)


class Search(Sorting):
    def __init__(self,data,key):
        self.data=data
        self.key=key
    def linearsearch(self):
        for i in range(len(self.data)):
            if(self.key==self.data[i]):
                print("Element Found")
                break
        else:
            print("Element is not Found")
    def binarysearch(self):
        self.selection_sort()
        l=0
        h=len(self.data)-1
        ic=0
        while(l<=h):
            ic+=1
            m=(l+h)//2
            if(self.data[m]==self.key):
                print("Element is Found")
                break
            elif(self.data[m]<self.key):
                l=m+1
            else:
                h=m-1
        else:
            print("Element Not found")
        print(ic)
                
obj=Search([34,55,32,65,22,43,54,12,11],55)
obj.binarysearch()








"""
ds:
binary search
selection sort
insertion sort
bubble sort
hashing
stack
queue
linkedlist

1 2 3 4 5 6 7 8 9 
"""
