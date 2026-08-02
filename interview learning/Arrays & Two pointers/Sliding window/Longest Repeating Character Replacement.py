class Solution(object):
    def characterReplacement(self, s, k):
        window={}
        left=0
        best=0
        max_freq=0
       
        for  right, char in enumerate (s):
            window[char]=window.get(char,0)+1
            max_freq=max(max_freq , window[char])

            window_size=right-left+1
            if window_size-max_freq>k:
                left_char=s[left]
                window[left_char]-=1
                left+=1
            best=max(best,right-left+1)
        return best

                                           