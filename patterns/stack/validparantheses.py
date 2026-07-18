class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                tp = st.pop()
                if tp != pairs[i]:
                    return False
        return len(st) == 0