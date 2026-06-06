# Normal Optimal
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        z = 0
        o = 0
        t = 0

        for i in nums:
            if i == 0:
                z += 1
            elif i == 1:
                o += 1
            else:
                t += 1


        nums[:] = [0]*z + [1]*o + [2]*t