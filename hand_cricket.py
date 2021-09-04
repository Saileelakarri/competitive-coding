def findstring(s):
    n=int(s)
    returnstring=""
    if n<0 or n>99:
        print("Invalid")
    else:
        d={0:"00000",1:"00001",2:"00011",3:"00111",4:"01111",5:"10000",6:"10001",7:"10011",8:"10111",9:"11111"}
        if len(s)==1:
            returnstring+="00000"+d[n]
        else:
            n1=int(s[0])
            n2=int(s[1])
            returnstring+=d[n1][::-1]
            returnstring+=d[n2]
    print(returnstring)
t=int(input())
for i in range(t):
    s=input()
    findstring(s)