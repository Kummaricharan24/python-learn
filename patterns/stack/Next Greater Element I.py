class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        st=[]
        for num in nums2:
            while st and  st[-1] < num :
                next_greater[st.pop()] = num
            st.append(num)
        return [next_greater.get(n,-1) for n in nums1]