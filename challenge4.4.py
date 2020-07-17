import time
start = time.process_time()

def multiples(l, index):
    current_divider = l[index]
    return [item for item in l[index + 1:] if item % current_divider == 0]


def dividers(l, index):
    current_dividend = l[index]
    return [item for item in l[:index] if current_dividend % item == 0]


def solution(l):
    list_size = len(l)
    count = 0
    while list_size >= 2:
        list_size -= 1
        count += len(dividers(l, list_size)) * len(multiples(l, list_size))

    return count

    
        
print(solution([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]))
print(time.process_time() - start)