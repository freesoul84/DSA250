class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = -1
        cnt = len(arr)-1
        while cnt != -1:
            val = arr[cnt]
            arr[cnt] = temp
            temp = max(val, arr[cnt])
            cnt -= 1
        return arr

        