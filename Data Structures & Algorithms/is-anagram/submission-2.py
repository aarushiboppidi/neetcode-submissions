class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        checks = {}
        checkt = {}

        for i in s:
            checks[i] = checks.get(i,0) + 1
        for i in t:
            checkt[i] = checkt.get(i,0) + 1

        if checks == checkt:
            return True
        else:
            return False

