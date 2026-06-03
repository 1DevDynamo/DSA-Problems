#We dont need to care about duplicates here

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        max_diff = float('inf')
        close_sum = float('inf')

        for fix in range(n-2) :

            l = fix +1
            r = n-1

            while l < r:

                curr_sum = nums[fix] + nums[l] + nums[r]
                diff = abs(target - curr_sum)

                if diff < max_diff:

                    max_diff = diff
                    close_sum = curr_sum


                if curr_sum == target:
                    return curr_sum

                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return close_sum


                