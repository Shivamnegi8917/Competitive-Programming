class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = 0
        for i in range(n):
            arr = arr^(start+2*i)
        return arr
