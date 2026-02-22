class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        for i in magazine:
            if i not in ransomNote_dict:
                ransomNote_dict[i] = 1
            else:
                ransomNote_dict[i] += 1
        
        for i in ransomNote:
            if i in ransomNote_dict:
                if ransomNote_dict[i] > 0:
                    ransomNote_dict[i] -= 1
                else:
                    return False
            else:
                return False
        return True
            