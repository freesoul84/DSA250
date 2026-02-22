class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        li = [i for i in allowed]
        cnt = 0
        for i in words:
            temp = [k for k in i]
            a = set(temp).intersection(set(li))
            if 0< len(a) <= len(li) and len(set(temp)) == len(set(a)):
                cnt += 1
            else:
                continue
        return cnt