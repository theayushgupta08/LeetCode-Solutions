class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum = 0
        while (n!=0):
            digit = n%10
            prod *= digit
            sum += digit
            n = n// 10
        return (prod-sum)
        