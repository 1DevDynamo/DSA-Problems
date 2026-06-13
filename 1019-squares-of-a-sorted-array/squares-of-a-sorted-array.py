# 2-pointer approach

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = 0
        right = n-1
        ans = n-1
        solu = [0]*n

        for i in range(0,n):
            l_sq = nums[left]*nums[left]
            r_sq = nums[right]*nums[right]

            if r_sq > l_sq:
                solu[ans] = r_sq
                right-= 1
                ans -= 1
            else:
                solu[ans] = l_sq
                left += 1
                ans -= 1
        return solu