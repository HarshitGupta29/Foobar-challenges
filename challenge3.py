def solution(s):
    s=s.replace("-","")
    test = list(s) 
    left=map(lambda x:int(1) if (x=="<") else int(0),test)
    right=map(lambda x:int(1) if (x==">") else int(0),test)
    left=left[::-1]
    t=0
    for i in range(0,len(s)):
        if (1==left[i]):
            k=left[i::]
            t+=k.count(0)
        if (1==right[i]):
            k=right[i::]
            t+=k.count(0)
    return t

salute=solution(">----<")
print(salute)
