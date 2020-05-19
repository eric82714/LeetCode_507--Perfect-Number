class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        
        tmp, divisor = num-1, 2
        
        while divisor * divisor < num:
            if num % divisor == 0:
                tmp = tmp - divisor - (num // divisor)              
            divisor += 1
            
        return tmp == 0
