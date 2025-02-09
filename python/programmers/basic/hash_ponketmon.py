# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    distinct_list = []
    N = nums.__len__() // 2
    for num in nums :
        if num not in distinct_list:
            distinct_list.append(num)
    if N > distinct_list.__len__() :   
        answer = distinct_list.__len__()
    else : 
        answer = N
    return answer


test_case_list = [[3,3,3,2,2,2],[1,2,3,4,5,6],[1,1,1,2,3,4],[2,2]]
for case in test_case_list :
    print(solution(case))
