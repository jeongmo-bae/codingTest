#https://school.programmers.co.kr/learn/courses/30/lessons/250136
"""
import sys
sys.setrecursionlimit(10**6)
def detect_petroleum(land, x, y, visited, coordinates_petroleum):
    if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or (x, y) in visited:
        return None
    else :
        visited.add((x, y))
        if land[x][y] == 1:
            coordinates_petroleum.add((x,y))
            detect_petroleum(land, x + 1, y, visited, coordinates_petroleum)
            detect_petroleum(land, x - 1, y, visited, coordinates_petroleum)
            detect_petroleum(land, x, y + 1, visited, coordinates_petroleum)
            detect_petroleum(land, x, y - 1, visited, coordinates_petroleum)
            return coordinates_petroleum
    return None


def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    info_all_chunks_of_petroleum = []
    visited = set()
    for y in range(m):
        sum_amount = 0
#        print(f"\n### y = {y} ###")
        for x in range(n):
#            print(f"\n### x = {x} ###")
            coordinates_petroleum = detect_petroleum(land, x, y, visited,set())
            if coordinates_petroleum :
                info_all_chunks_of_petroleum\
                    .append(
                    [min(coordinates_petroleum, key=lambda x: x[1])[1],
                     max(coordinates_petroleum, key=lambda x: x[1])[1],
                     len(coordinates_petroleum)]
                )
#            print(coordinates_petroleum)
#            print(info_all_chunks_of_petroleum)

        for chunk in info_all_chunks_of_petroleum :
            if y >= chunk[0] and y <= chunk[1] :
                sum_amount += chunk[2]
        answer = max(answer, sum_amount)

    return answer
"""

from collections import deque

def detect_petroleum(land, x, y, visited):
    """BFS로 석유 덩어리를 탐색하고, (왼쪽 끝 열, 오른쪽 끝 열, 크기) 반환"""
    n, m = len(land), len(land[0])
    queue = deque([(x, y)])
    visited.add((x, y))  # 방문 체크를 여기서 먼저!
    coordinates_petroleum = [(x, y)]
    left, right = y, y  # 왼쪽 끝, 오른쪽 끝 열 정보

    while queue:
        print('queue : ',queue)
        print('visited : ',visited)
        print('coordinates_petroleum : ',coordinates_petroleum)
        cx, cy = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and land[nx][ny] == 1:
                queue.append((nx, ny))
                visited.add((nx, ny))
                coordinates_petroleum.append((nx, ny))
                left = min(left, ny)
                right = max(right, ny)

    return (left, right, len(coordinates_petroleum))  # (왼쪽 끝, 오른쪽 끝, 크기)

def solution(land):
    """가장 많은 석유를 수집할 수 있는 열의 합 구하기"""
    n, m = len(land), len(land[0])
    answer = 0
    visited = set()  # 방문 체크는 set으로 O(1) 탐색
    # 모든 석유 덩어리 정보 저장
    oil_chunks = []
    for x in range(n):
        for y in range(m):
            if (x, y) not in visited and land[x][y] == 1:
                oil_chunks.append(detect_petroleum(land, x, y, visited))

    # 각 열(y)마다 포함되는 석유의 합을 미리 계산
    oil_sums = [0] * m  # 각 열(y)에서 포함되는 석유의 합
    for left, right, size in oil_chunks:
        for y in range(left, right + 1):
            oil_sums[y] += size  # 해당 범위 내 모든 y에 대해 크기 추가

    # 가장 큰 값 찾기
    answer = max(oil_sums)

    return answer

iter = 0
test_cases = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]

for case in test_cases :
    iter += 1
    print(f"\n### testcases{iter}")
    print("ANSWER : ",solution(case))


