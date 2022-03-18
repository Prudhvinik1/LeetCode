class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        all_chars = {}
        for i in s:
            if i in all_chars:
                all_chars[i] +=1
            else:
                all_chars[i] = 1
        print(all_chars)        
        cnt=0
        for i in (all_chars):
            cnt += (all_chars[i]//2) *2
            if cnt%2==0 and all_chars[i]%2 == 1:
                cnt+=1
        return cnt