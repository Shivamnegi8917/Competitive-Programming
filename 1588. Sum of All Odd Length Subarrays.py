class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # ans--> number of subarrays with odd sum
        ans = 0
        
        # Taking all n^2 subarrays,taking odd length and finding their sum
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                l = j-i+1
                # odd length subarray
                if l%2!=0:
                    ans+=sum(arr[i:j+1:])
        return ans
        
