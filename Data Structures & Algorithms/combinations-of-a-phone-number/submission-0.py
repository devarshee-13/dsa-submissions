class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9': 'wxyz'
        }
        res = []
        def backtrack(i, s):
            if not digits: return []

            if len(s) == len(digits): 
                res.append(s)
                return

            for each in digitToChar[digits[i]]:
                backtrack(i+1, s+each)

        backtrack(0,"")
        return res
