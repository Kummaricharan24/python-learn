from collections import Counter 
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len (p)> len(s):
            return []
        result=[]
        p_count=Counter(p)
        window_count=Counter(s[:len(p)])
        if window_count==p_count:
            result.append(0)
        for i in range (len(p),len(s)):
            left_char=s[i-len(p)]
            right_char=s[i]
            window_count[right_char]+=1
            window_count[left_char]-=1
            if window_count[left_char]==0:
                del window_count[left_char]
            if window_count == p_count:
                result.append(i-len(p)+1)
        return result
