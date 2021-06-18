class Solution:
    
    def search(self , nums , target):
        # write code here
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1
        low = 0
        higth = len(nums) -1
        mid = 0
        while(low <= higth):
            mid = low + (higth - low) / 2
            if (nums[mid] == target):
                while(mid!=0 and nums[mid-1] == nums[mid]):
                    mid = mid - 1
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1