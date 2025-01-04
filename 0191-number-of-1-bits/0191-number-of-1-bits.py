class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = 0
        count = 0
        while (n!=0):
            rem = n%2
            if(rem):
                count +=1
            binary = (binary * 10) + rem
            n = n//2
        # while(binary !=0):
        #     digit = binary % 10
        #     if (digit):
        #         count +=1

        return count