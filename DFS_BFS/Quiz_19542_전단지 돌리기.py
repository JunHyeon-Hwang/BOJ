"""
문제
현민이는 트리 모양의 길 위에서 오토바이를 타고 전단지를 돌리려고 한다. 
현민이의 목표는 케니소프트에서 출발하여 모든 노드에 전단지를 돌리고, 다시 케니소프트로 돌아오는 것이다. 
현민이는 힘이 좋기 때문에 현재 노드에서 거리가 $D$ 이하인 모든 노드에 전단지를 돌릴 수 있다.

날씨가 매우 덥기 때문에, 현민이는 최소한만 이동해서 목표를 달성하고 싶다! 현민이를 위해 현민이가 이동해야 하는 총 거리를 구해주자.

입력
첫번째 줄에는 노드의 개수 $N$($ 1 \leq N \leq 100\ 000 $)과 케니소프트의 위치 $S$($ 1 \leq S \leq N $), 힘 $D$($ 0 \leq D \leq N $)이 주어진다.

두 번째 줄부터 $N$번째 줄까지, 트리의 간선 정보를 의미하는 두 자연수 $x$, $y$가 공백으로 구분되어 주어진다. 
이는 $x$번 노드와 $y$번 노드가 연결되어 있음을 의미한다. ($1 \leq x, y \leq N$, $x \neq y$)

주어지는 연결관계는 트리를 구성하며, 모든 간선의 길이는 $1$이다.

출력
현민이가 목표를 완수하기 위해 이동해야 하는 최소 거리를 출력하여라.
====================================================================================================================================================================================
DFS한 후 해당 노드에서 D만큼만 BFS한다면?? 
DFS하는 후보군은 BFS 한 결과에서 더 탐색이 필요한 곳으로만 간다.
ㄴ> 양방향 그래프이기 때문에 구현하기 쉽지 않고 시간 복잡도 면에서도 쉽지 않다.

💥 DFS 두 번으로 끝낼 수 있다.
최초 DFS를 통해서 SuubTree의 depth를 기록한다. 

SubTree Depth를 기록한 후 
각 SubTree가 D보다 깊으면 이 곳은 탐색이 필요하기에 DFS 진행하고 
depth 가 D보다 작거나 같다면 굳이 이동하지 않고 던져서 전단지를 전달할 수 있다.

따라서 DFS 두 번으로 해결가능하다. 
💥 Pypy3 으로 AC

ㄴ> DFS 한 번으로도 해결가능하다고 한다.
"""

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

N, S, D = map(int, input().split())
graph = defaultdict(list)
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
subTreeDepth = [0]*(N+1)
visited = [False] * (N+1)
def SetSubTreeDepth(now):
    global subTreeDepth
    depth = 1
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            depth = max(SetSubTreeDepth(nxt), depth)
    
    subTreeDepth[now] = depth    
    return depth +1

SetSubTreeDepth(S)

visited = [False] * (N+1)
result = 0
def DFS(now):
    global result
    visited[now] = True
    
    for nxt in graph[now]:
        if not visited[nxt] and subTreeDepth[nxt] > D:
            result += 1
            DFS(nxt)

DFS(S)
print(result*2)