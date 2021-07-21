class Stack:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.data=[-1 for _ in range(size)]
    def push(self,val):#top-1
        if self.top==self.size-1:#-1==5
            print("Stack Overflow")
        else:
            self.top+=1#0
            self.data[self.top]=val# 100 -1 -1 -1 -1 -1
            
    def pop(self):
        if self.top==-1:
            print("stack Under flow")
        else:
            val=self.data[self.top]
            self.data[self.top]=-1
            self.top-=1
            return val
    def display(self):
        if self.top==-1:
            print("stack Under flow")
        else:
            for i in range(self.top,-1,-1):
                print(self.data[i])
        
    
stack=Stack(6)
stack.push(100)
stack.push(200)
stack.push(400)
stack.push(300)
stack.push(600)
stack.push(1000)
stack.push(20)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())



