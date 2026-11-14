class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        t = t.replace(" ", "")
        t = "".join(filter(str.isalnum,t))
        point = len(t)-1
        for i in range(len(t)):
            if t[i] != t[point]:
                return False
            point-=1
         
        return True