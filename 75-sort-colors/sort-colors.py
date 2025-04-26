class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = len([i for i in nums if i == 0])
        b = len([i for i in nums if i == 1])
        c = len([i for i in nums if i == 2])
        i = 0
        while i<a:
            nums[i] = 0
            i += 1

        j = i 
        while j < a+b:
            nums[j] = 1
            j += 1

        k = j 
        while k < a+b+c:
            nums[k] = 2
            k+= 1

        return  nums