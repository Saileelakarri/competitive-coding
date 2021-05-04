class Solution:
    def searchInsert(self, nums: List[int], target: int): 
        n=len(nums)
        
        #if target is already present in given array, return the position of the target
        if target in nums:
            return nums.index(target)
          
        #if target is greater than the largest element in array, return last position
        elif target>nums[n-1]:
            return n
          
        # if target is smaller than the smallest element in array, return index 0
        elif target<nums[0]:
            return 0
          
        #else search for the position in array using binary search  
        else:
            left=0
            right=n-1
            mid=(left+right)//2
            while left<right:
                if nums[mid]<target and nums[mid+1]>target:
                    return mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
                if left==right:
                    return left+1
                mid=(left+right)//2
                
