class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st=[]
        for i, temp in enumerate(temperatures):
            while st and temp > temperatures[st[-1]]:
                old_index = st.pop()
                result[old_index] = i - old_index
            st.append(i)
        return result
