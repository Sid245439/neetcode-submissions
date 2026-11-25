class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check_arr = [0]*26

        for i in range(len(s)):
            check_arr[ord(s[i])-ord('a')] += 1
            check_arr[ord(t[i])-ord('a')] -= 1
        
        for val in check_arr:
            if val != 0:
                return False
        
        return True


        