# python-learn-
class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for part in path.split("/"):
            if part == "" or part ==".":
                continue 
            elif part=="..":
                if st:
                    st.pop()
            else:
                st.append(part)
        return "/" + "/" .join(st)
            