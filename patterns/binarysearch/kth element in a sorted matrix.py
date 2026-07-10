class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessEqual(mid):
            count=0
            rows=n-1
            cols=0
            while rows>=0 and cols <n:
                if matrix[rows][cols] <= mid:
                    count+=rows+1
                    cols+=1
                else:
                    rows-=1
            return count
        n=len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        while low<high:
            mid=(low+high)//2
            if countLessEqual(mid)<k:
                low = mid + 1
            else:
                high=mid
        return low
s1=Solution()
print(s1.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], k = 8))

        