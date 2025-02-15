from pccp_kichul_1_1 import solution as solution_1_1
from pccp_kichul_1_2 import solution as solution_1_2
from pccp_kichul_1_3 import solution as solution_1_3
print(solution_1_1)
def check_solution(test_cases, function):
    _iter = 0
    print('\n',function)
    for case in test_cases:
        _iter += 1
        print(f"\n### testcases{_iter}")
        print("ANSWER : ", function(case))
"""
test_cases = [
    [[5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]],
    [[3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]],
    [[4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]],
    [[1, 1, 1], 5, [[1, 2], [3, 2]]]
]
print(check_solution(test_cases,solution_1_1))
"""
test_cases = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]
check_solution(test_cases,solution_1_2)

print('\n### kichul_1_3 testcases')
print(solution_1_3(0, 5, 30, 0, 7, 0))