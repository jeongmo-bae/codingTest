# https://school.programmers.co.kr/learn/courses/30/lessons/250136

def detect_petroleum(land,x,y,visited) :
    if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or [x,y] in visited:
        return 0
    else :
        visited.append([x,y])
        if land[x][y] == 1 :
            return 1 + detect_petroleum(land,x+1,y,visited) + detect_petroleum(land,x-1,y,visited) + detect_petroleum(land,x,y+1,visited) + detect_petroleum(land,x,y-1,visited)
        else : 
            return 0
        
def solution(land):
    answer = 0
    for y in range(len(land[0])) : 
        sum = 0
        visited = []
        for x in range(len(land)) :
            sum = sum +  detect_petroleum(land,x,y,visited) 
#        print("[",y,"] :::",sum)
        if answer < sum : 
            answer = sum
    return answer

### 효율성 테스트 실패함 ;;;

iter = 0
test_cases = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]

for case in test_cases :
    iter += 1
    print(f"\n### testcases{iter}")
    print("ANSWER : ",solution(case))