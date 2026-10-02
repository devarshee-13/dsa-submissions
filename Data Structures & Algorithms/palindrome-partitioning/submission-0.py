class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []

        def isPalindrome(l,r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            else: return True

        def backtracking(start):
            if start >= len(s):
                res.append(substring[:])
                return

            for i in range(start,len(s)):
                if isPalindrome(start,i):
                    substring.append(s[start:i+1])
                    backtracking(i+1)
                    substring.pop()
        backtracking(0)
        return res     