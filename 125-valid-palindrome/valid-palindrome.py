class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        s = ''.join([i for i in s if (ord(i)>=97 and ord(i)<=122) or i.isnumeric()])
        print(s)
        return s == s[::-1]