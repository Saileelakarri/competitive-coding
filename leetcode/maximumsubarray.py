class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #supporting array to store the sum values
        l=[]
        l.append(nums[0])
        for i in range(1,len(nums)):
            cur_sum=l[i-1]+nums[i]
            l.append(max(cur_sum,nums[i]))
        return max(l)    
           
