#https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    right = n * times[-1]
    while left <= right :
        capacity = 0
        mid = (left + right)//2
        for time in times :
            capacity += mid // time 
        if capacity >= n :
            right = mid -1
            answer = mid
        else :
            left = mid+1
            
    return answer
print(solution(6, [7, 10]))