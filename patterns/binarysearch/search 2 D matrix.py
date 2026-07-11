class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows=len(matrix)
        cols=len(matrix[0])
         
        left=0
        right=rows*cols-1
        while left<=right:
            mid=left+(right-left)//2
            row=mid//cols
            col=mid%cols
            mid_val=matrix[row][col]
            if mid_val==target:
                return True
            elif mid_val<target:
                left=mid+1
            else:
                right=mid-1
        return False
s1=Solution()
print(s1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))