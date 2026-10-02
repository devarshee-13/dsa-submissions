class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}
        mem[0] = 0
        mem[1]=1
        mem[2]=1
        def dfs(cur):
            if cur in mem:
                return mem[cur]

            mem[cur] = dfs(cur-1) + dfs(cur-2) + dfs(cur-3)
            return mem[cur]
        return dfs(n) 