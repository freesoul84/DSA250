class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        val = int(''.join(digits)) + 1
        result = [i for i in str(val)]
        return [int(i) for i in result]