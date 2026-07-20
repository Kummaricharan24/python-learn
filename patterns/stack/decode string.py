class Solution:
    def decodeString(self, s: str) -> str:
        def func(i):
            string=n=''
            while i<len(s):
                x=s[i]
                i+=1
                if x=="]":
                    return string, i
                elif x=="[":
                    multi,i=func(i)
                    string +=int(n)* multi
                    n=" "
                elif x.isdigit():
                    n+=x
                else:
                    string +=x
            return string
        return func(0)
