class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # vairable window size
        n = len(nums)
        low = 0
        high = 0
        tsum = 0
        res = float('inf')

        while high < n:
            tsum += nums[high]

            while tsum >= target:
                tsum -= nums[low]
                leng = high - low +1
                res = min(res,leng)
                low += 1
            high +=1
        if res == float('inf'):
            return 0
        else:
            return res