def solution(pegs):
    k=0
    temp=-1
    for i in range(1,100):
      
      for b in range(1,i+1):  
        
        temp=pegs[1]-(i/b)-pegs[0]
        if (temp<1):
                l=[-1,-1]
                break
        for j in range(1,len(pegs)-1):
            temp=pegs[j+1]-temp-pegs[j]
            l=[i,b,temp]
            k=i/b
            print(l)
            if (temp<1):
                l=[-1,-1]
                break
            elif(k==(temp*2)):
                return l 
    if(k!=(temp*2)):
        l=[-1,-1]
    return l
l=solution([4,30,50])
print(l)