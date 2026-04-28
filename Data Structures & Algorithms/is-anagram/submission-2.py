class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # easy edge cases
        # 1. if they are the same word
        # 2. if the lengths are diff then not anagrams
        if s == t:
            return True
        if len(s) != len(t):
            return False
        
        # HashMaps for each word
        sMap = {}
        tMap = {}

        # Fill HashMaps
        for i in range(0, len(s)):
            sMap[s[i]] = sMap[s[i]] + 1 if s[i] in sMap else 1
            tMap[t[i]] = tMap[t[i]] + 1 if t[i] in tMap else 1

        # Compare Hashmaps
        ## Apparently you can straight up compare Hashmaps in Python
        return sMap == tMap

        ## Manual HashMap comparison (slightly slower)
        # for char in sMap:
        #     if char not in tMap or sMap[char] != tMap[char]:
        #         return False
        # return True


        