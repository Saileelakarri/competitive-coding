class Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.data=[]
    def enqueue(self,val):
        if self.rear==self.size-1:
            print("Queue is FULL")
        else:
            if(self.rear==-1 and self.front==-1):
                self.rear=0
                self.front=0
            else:
                self.rear+=1
            self.data.append(val)
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")
        else:  
            if(self.rear==self.front):
                self.rear=-1
                self.front=-1
            else:
                self.rear-=1
            self.data.pop(0)
            
    def display(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.data[i])
queue=Queue(6)

