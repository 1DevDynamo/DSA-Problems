# Brute force
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        z = []
        o = []
        t = []

        for num in nums:
            if num == 0:
                z.append(num)
            elif num == 1:
                o.append(num)
            else:
                t.append(num)

        nums[:] = z + o + t