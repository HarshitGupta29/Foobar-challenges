import time
start = time.process_time()
def answer(map, git_gud=True):

    if git_gud:
        success, result = fast_answer(map)
        if success:
            return result

    w, h = (len(map[0]), len(map))
    inf = w*h+1
    vs = [Vertex(map[i/w][i % w], i, w, inf=inf) for i in range(h*w)]
    q = range(w*h)  # set of unvisited vertices
    vs[0].set_start()  # set start distance to 1 to count inclusive
    target = h*w - 1  # set target vertex index

    cnt = 0
    while len(q) > 0:
        cnt += 1
        min_dist, min_idx = find_min_dist(q, vs, inf)
        el = q[min_idx]  # index of the min_dist unvisted vertex
        if el == target:  # winner
            # print("Total tries: {}".format(cnt))
            break
        if min_dist.get_walls() == 0:
            del q[min_idx]

        u = vs[el].visit(min_dist.get_walls())
       
        for n in u.neighbors(vs, min_dist.get_walls()):
            n.update_dist(min_dist, el)

    if inf == min_dist.get_dist():
        raise RuntimeError  
    return min_dist.get_dist()

k=answer([[0, 0, 0, 0,0,0,0,0], [1, 1, 1, 1, 1,1,1, 0],[1, 1, 1, 1, 1,1,1, 0],[1,0,0,0,0,1,1,0],[0,1,1,1,0,0,0,0],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0, 0, 0, 0, 0, 0,0,0]])
print(k)

print(time.process_time() - start)