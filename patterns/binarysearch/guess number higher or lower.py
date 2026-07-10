class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<=right:
            mid=left+(right-left)//2
            # The API provided by the problem is `guess(num)`, not `guessNumber`.
            result = guess(num)
            if result==0:
                return mid
            elif result == -1:
                right=mid-1
            else:
                left=mid+1
        return -1
s1=Solution()
print(s1.guessNumber(n = 10))