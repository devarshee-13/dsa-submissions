class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=2:
            return 1 if n!=0 else 0
        prev0 = 0
        prev1 = 1
        prev2 = 1
        for i in range(3,n+1):
            cur = prev0+prev1+prev2
            prev0=prev1
            prev1=prev2
            prev2=cur
       
        return cur