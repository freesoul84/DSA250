class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) == len(t):
            for i in s:
                if i not in dictionary:
                    dictionary[i] = 1
                else:
                    dictionary[i] += 1
            
            for i in t:
                if i not in dictionary:
                    return False
                else:
                    dictionary[i] -= 1
                    if dictionary[i] <0 :
                        return False
            else:
                return True
        else:
            return False