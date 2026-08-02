from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need=Counter(t)
        have=0
        window={}
        required=len(need)
            
        best_len=float("inf")
        best_left=0
        left=0
        for right , char in enumerate(s):
            window[char]=window.get(char,0)+1
            if char in need and window[char]==need[char]:
                have+=1
            while have==required:
                if (right-left+1)<best_len:
                    best_len=right-left+1
                    best_left=left
                left_char=s[left]
                window[left_char]-=1
                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                left+=1
        return ""if best_len==float("inf")else s[best_left:best_left+best_len]

                    