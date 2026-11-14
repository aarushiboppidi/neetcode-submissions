class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i
        
        new = new.strip()
        new = new.lower()

        point = len(new)-1
        for i in range(len(new)):
            if new[i] != new[point]:
                return False
            point-=1
         
        return True