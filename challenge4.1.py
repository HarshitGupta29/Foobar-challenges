import numpy as np
import time
start = time.process_time()
   
def possible(e,w,h,s,blocked,done,distance):
  if ((e[0]+w)>=0) and ((e[1]+h)>=0):  
    if ((e[3]==1) and (s[e[0]+w][e[1]+h]==1)) or (blocked[e[0]+w][e[1]+h]==1) or (distance[e[0]+w][e[1]+h]<(e[2]+1)):
        return False
    elif (done[e[0]+w][e[1]+h]==1):
        return False
    else:
        return True
  else:
      return False
    
def blocked_find(s):
    blocked=np.zeros([len(s),len(s[0])])
    k=np.pad(s,((1,1),(1,1)),mode='constant',constant_values=1)
    for i in range (1,len(s)+1):
        for j in range (1,len(s[0])+1):
            t=0
            for r in [[-1,0],[1,0],[0,-1],[0,1]]:
                if (k[i+r[0]][j+r[1]]==1):
                    t+=1
            if (t>=3) and (k[i][j]==1): 
                 blocked[i-1][j-1]=1 
    blocked[0][0]=0
    blocked[len(s)-1][len(s[0])-1]=0
    done=np.zeros([len(s),len(s[0])])
    distance=np.full((len(s),len(s[0])),1000)
    queue=[[0,0,1,0]]
    for element in queue:
        for r in [[-1,0],[1,0],[0,-1],[0,1]]:
                if (possible(element,r[0],r[1],s,blocked,done,distance)):
                    if (s[element[0]+r[0]][element[1]+r[1]]==1)and (element[3]==0):
                        wall=1
                    else:
                        wall=0
                    distance[element[0]+r[0]][element[1]+r[1]]=element[2]+1
                    queue.append([element[0]+r[0],element[1]+r[1],element[2]+1,element[3]+wall])
        
        done[element[0]][element[1]]=1


    return distance[len(s)-1][len(s[0])-1]

    
    

max=blocked_find([[0,1,1,1,0,0,1,1],[0,1,1,0,1,1,0,0],[0,0,0,0,1,0,0,1],[1,1,1,1,0,0,1,1],[0,1,1,0,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0]])
print(max)
print(time.process_time() - start)