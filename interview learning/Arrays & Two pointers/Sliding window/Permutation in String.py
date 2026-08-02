from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        need=Counter(s1)
        left=0
        window={}  
        
        for right,char in enumerate(s2):
            window[char]=window.get(char,0)+1
            window_size=right-left+1
            if window_size>len(s1):
                left_char=s2[left]
                window[left_char]-=1
                if window[left_char]==0:
                    del window[left_char]
                left+=1 
            if (right-left+1 )==len(s1) and window==need:
                return True
        return False




            