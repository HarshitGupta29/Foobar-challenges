import numpy as np
def blocked_find(s):
    h=len(s)
    w=len(s[0])
    blocked=np.zeros([h,w])
    for i in range(0,h):
        for j in range(0,w):

            try:

             if (s[i+1][j]==1) and (s[i][j+1]==1):

                blocked[i][j]=1      
            except IndexError:
                continue
    return blocked



def solution(map):
    min=0
    blocked=blocked_find(map)
    print(blocked)
    return min
l=solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print(min)