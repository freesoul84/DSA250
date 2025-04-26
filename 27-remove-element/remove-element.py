class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
        
        for i in range(len(nums)-1):
            for i in range(len(nums)-1-i):
                if nums[i] == "_":
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        
        return len([i for i in nums if i!='_'])