#https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""
from itertools import combinations

def solution(distance, rocks, n):
    answer = 0
    n_rocks = rocks.__len__()
    for comb in combinations(rocks, n_rocks - n):
        work_rocks = list(comb)
        work_rocks.sort()
        print('work_rocks : ',work_rocks)
        distance_list = []
        for i in range(len(work_rocks) + 1):
            if i == 0:
                distance_list.append(work_rocks[i] - 0)
            elif i == len(work_rocks):
                distance_list.append(distance - work_rocks[i - 1])
            else:
                distance_list.append(work_rocks[i] - work_rocks[i - 1])
        print('distance_list : ', distance_list)
        print('min_distance_list : ', min(distance_list))
        answer = max(answer,min(distance_list))
        print(answer)
    return answer
"""

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left = 1
    right = distance
    while left <= right :
        mid = (left + right)//2
        prev_rock = 0
        delete = 0
        for rock in rocks :
            dist = rock - prev_rock
            if dist < mid :
                delete += 1
                if delete > n:
                    break
            else :
                prev_rock = rock

        if delete > n :
            right = mid-1
        elif delete <= n :
            left = mid + 1
            answer = mid

    return answer

solution(25, [2, 14, 11, 21, 17], 2)