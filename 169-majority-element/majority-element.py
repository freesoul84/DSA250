class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        
        k,v = 0, 0
        for i in dictionary:
            print(i,dictionary[i],v)
            if dictionary[i] > v:
                v = dictionary[i]
                k = i
        else:
            return k