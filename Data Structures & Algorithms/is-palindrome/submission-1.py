class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. remove spaces, remove non-Alphanumeric characters, all lower case
        s2 = "".join(char for char in s if char.isalnum()).lower()
        # print(s2)

        # Two options
        ## Reverse string and compare if equal (utilizes functions)
        # return s2 == s2[::-1]

        ## manually iterate thru half the string and compare against back half
        for i in range(0, len(s2)//2):
            if s2[i] != s2[len(s2)-1-i]:
                return False
        return True
