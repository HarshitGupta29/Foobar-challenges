import time
start = time.process_time()
def solution(entrances, exits, path):
    h=len(path)
    w=len(path[0])
    total_w=[0 for i in range(0,w)]
    total_h=[0 for i in range(0,h)]
    for j in entrances:
        for i in range(0,w):
            total_w[i]+=path[j][i]
            if i!=j:
                total_h[i]=sum(path[i])
    total=0
    for i in range(0,len(total_h)):
        total+=min(total_h[i],total_w[i])
    return total




print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(time.process_time() - start)