class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF       # 8 F's. used to convert (-ve) to (+ve)
        for i in range(32):
            a_bit = (a>>i) & 1
            b_bit = (b>>i) & 1

            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit+b_bit+carry) >= 2

            if cur_bit:
                res = res | (1<<i) 
        
        if res > 0x7FFFFFFF:        # 7 F's. used to check if res is -ve. this 0x7FFFFFFF is the max +ve no. in 32-bits no. anything more than that is -ve
            res = ~(res^mask)
        return res