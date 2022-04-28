"""
문제
총 25명의 여학생들로 이루어진 여학생반은 5×5의 정사각형 격자 형태로 자리가 배치되었고, 
얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다. 
곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 
얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.

위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. 
‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.

이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.

입력
'S'(이다‘솜’파의 학생을 나타냄) 또는 'Y'(임도‘연’파의 학생을 나타냄)을 값으로 갖는 5*5 행렬이 공백 없이 첫째 줄부터 다섯 줄에 걸쳐 주어진다.

출력
첫째 줄에 ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 출력한다.
============================================================================================================================================================================

🔥 Point
- Combination : 좌표를 선택해 경로 탐색 최소화
- 조합 중 S가개 3개 이하라면 한 번 걸러준다. => 탐색 진행하지 않는다.
- DFS 진행 : 조합에 해당하는 경우만 탐색하고 만난 학생이 7명이면 위 조건에 모두 만족하게 된다.
"""
from itertools import combinations


seats = [list(map(str, input())) for _ in range(5)]
## 위 오른쪽 아래 왼쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def dfs(now, pos_points, visited, cnt):
    global result
    if cnt == 7:
        result += 1

    x, y = now//5, now%5
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if 0<=nx<5 and 0<=ny<5 and not visited[5*nx+ny]:
            if pos_points.__contains__(5*nx+ny):
                visited[5*nx+ny] = True
                cnt = dfs(5*nx+ny, pos_points, visited,cnt+1)

    
    return cnt





candidate = list(combinations([i for i in range(25)], 7))
for cand in candidate:
    pos_points = set()
    visited = [False] * 25
    cnt_s = 0
    for i, c in enumerate(cand):
        if i == 0:
            start = c
            visited[c] = True
        pos_points.add(c)
        if seats[c//5][c%5]=='S':
            cnt_s += 1
            
    if cnt_s <= 3: continue
    dfs(start, pos_points, visited, 1)

print(result)
