class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        un = 1       # first element is unique

        p1 = 0       # pointer which moves only on unique element to count them

        p2 = 1       # second pointer movies till n to check uniqueness and because first elemet is already uniquw p2=1

        while(p2 < len(nums)):

            if nums[p2] == nums[p2-1]:
                p2 +=1
            
            else:
                nums[p1+1] = nums[p2]
                un += 1
                p1 += 1
                p2 += 1
        
        return un
