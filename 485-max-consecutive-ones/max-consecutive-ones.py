class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        for i in range(len(nums)-1):
            print(nums[i], nums[i+1], cnt, max_cnt)
            if nums[i] == nums[i+1] == 1:
                cnt+=1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        max_cnt = max(max_cnt, cnt)
        return max_cnt+1 if len(nums)>0 and 1 in nums else max_cnt