class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,sid = 0,0,0
        solu = [0] *(m+n)
        while i < m and j < n:
            
            # i and j are pointers for both array and should not out of index so looping upto i,j<m,n
            if nums1[i] < nums2[j]:
                solu[sid] = nums1[i]
                i += 1
                sid  += 1
            else:
                solu[sid] = nums2[j]
                j += 1
                sid += 1
            
        while i < m:
            solu[sid] = nums1[i]
            i += 1
            sid += 1
        
        while j < n:
            solu[sid] = nums2[j]
            j += 1
            sid += 1

        nums1[:] = solu 