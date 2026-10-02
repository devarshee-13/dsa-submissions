class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i,c in enumerate(s):
            if c =='(': left.append(i)
            elif c =='*': star.append(i)
            else:
                if not left and not star:
                    return False
                if left: left.pop()
                else: star.pop()
        

        while left:
            if left and not star: return False
            elif left.pop() > star.pop(): return False
        
        return True

