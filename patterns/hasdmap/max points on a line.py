from math import gcd
from collections import defaultdict
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n <=2:
            return n
        max_points=1
        for i in range(n):
            slopes=defaultdict(int)
            duplicates=0
            local_max=0
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dx=x2-x1
                dy=y2-y1
                if dx == 0 and dy == 0:
                    duplicate+=1
                    continue 
                g=gcd(dx,dy)
                dx//=g
                dy//=g   
                if dx<0:
                    dx, dy = -dx, -dy
                elif dx==0:
                    dy=abs(dy)
                key=(dx,dy)
                slopes[key]+=1
                local_max=max(local_max, slopes[key])
            max_points=max(max_points, local_max+duplicates+1)
        return max_points         