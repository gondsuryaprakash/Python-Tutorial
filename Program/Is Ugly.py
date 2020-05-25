class Solution:
    def maxDivide(self, a, b):
        while a % b == 0:
            a = a / b
        return a

    def isUgly(self, num: int) -> bool:
        num = self.maxDivide(num, 2)
        num = self.maxDivide(num, 3)
        num = self.maxDivide(num, 5)

        return True if num == 1 else False
