class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        pos = [i for i in nums if i >= 0]
        neg = [i for i in nums if i < 0]

        pos = [i**2 for i in pos]
        neg = [i**2 for i in neg]

        neg = neg[::-1]

        m = len(pos)
        n = len(neg)

        i,j,sid = 0,0,0
        solu = [0] *(m+n)

        while i<m and j<n:
            
            if pos[i] < neg[j]:
                solu[sid] = pos[i]
                sid += 1
                i += 1
            else:
                solu[sid] = neg[j]
                sid += 1
                j += 1
        while i < m:
            solu[sid] = pos[i]
            sid += 1
            i += 1
        
        while j < n:
            solu[sid] = neg[j]
            sid += 1
            j += 1
        
        return solu