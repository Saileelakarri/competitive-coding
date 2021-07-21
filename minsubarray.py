arr=list(map(int,input("enter the list").split()))
k=int(input("enter the value to be checked"))
i=0
for j in range(len(arr)):
    cur_sum=0
    while cur_sum<k:
        cur_sum+=arr[j]
        
        
  for i in range(n):
        curr_sum = arr[i]
    
        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:
        
            if curr_sum == sum_:
                print ("Sum found between")
                print("indexes % d and % d"%( i, j-1))
                
                return 1
                
            if curr_sum > sum_ or j == n:
                break
            
            curr_sum = curr_sum + arr[j]
            j += 1

    print ("No subarray found")
    return 0
      
    

         
