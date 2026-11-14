class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_map = {}

        for word in strs:
            alphabetical = "".join(sorted(word))
            if alphabetical not in word_map:
                word_map[alphabetical] = []
            word_map[alphabetical].append(word)
            
        return list(word_map.values())