class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        st = []
        n = len(heights)
        for i in range(n):                     # fixed: was range(heights)
            while st and heights[st[-1]] > heights[i]:
                height = heights[st.pop()]
                if st:
                    width = i - st[-1] - 1
                else:
                    width = i
                area = height * width
                max_area = max(max_area, area)
            st.append(i)
        while st:
            height = heights[st.pop()]
            if st:
                width = n - st[-1] - 1
            else:
                width = n
            area = height * width
            max_area = max(max_area, area)
        return max_area