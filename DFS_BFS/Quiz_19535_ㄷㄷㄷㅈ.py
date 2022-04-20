"""
문제
어느 날, 트리를 물끄러미 보고 있던 동현이는 엄청난 사실을 하나 발견했다. 바로 정점이 네 개인 트리는 ‘ㄷ’과 ‘ㅈ’의 두 종류밖에 없다는 사실이다!



정점이 네 개 이상 있는 임의의 트리에 대해, 그 트리에서 정점 네 개로 이루어진 집합을 고르자. 전체 트리의 간선들 중 집합에 속한 두 정점을 잇는 간선만을 남겼을 때, 네 개의 정점이 하나의 트리 형태로 이어지게 된다면 ‘ㄷ’ 모양이거나 ‘ㅈ’ 모양일 것이다. 트리에서 ‘ㄷ’의 개수와 ‘ㅈ’의 개수를 각각 트리에서 ‘ㄷ’ 모양, ‘ㅈ’ 모양을 이루는 정점 네 개짜리 집합의 개수라고 하자.

이제, 동현이는 세상의 모든 트리를 다음과 같은 세 종류로 나누었다.

D-트리 : ‘ㄷ’이 ‘ㅈ’의 $3$배보다 많은 트리
G-트리 : ‘ㄷ’이 ‘ㅈ’의 $3$배보다 적은 트리
DUDUDUNGA-트리 : ‘ㄷ’이 ‘ㅈ’의 정확히 $3$배만큼 있는 트리
신이 난 동현이는 트리만 보이면 그 트리에 있는 ‘ㄷ’과 ‘ㅈ’이 몇 개인지 세고 다니기 시작했다. 하지만 곧 정점이 $30$만 개나 있는 트리가 동현이 앞에 나타났고, 동현이는 그만 정신을 잃고 말았다. 동현이를 대신해 주어진 트리가 D-트리인지 G-트리인지 아니면 DUDUDUNGA-트리인지 알려주자!

입력
첫 번째 줄에 트리의 정점 수 $N$이 주어진다. ($4 \leq N \leq 300\ 000$)

두 번째 줄부터 $N-1$개의 줄에 트리의 각 간선이 잇는 두 정점의 번호 $u$, $v$가 주어진다. ($1 \leq u, v \leq N$)

출력
첫 번째 줄에 주어진 트리가 D-트리라면 D, G-트리라면 G, DUDUDUNGA-트리라면 DUDUDUNGA를 출력한다.
==================================================================================================================================================================

DFS 과정 중 경로의 길이가 4 라면 ㄷ을 만들 수 있고
                길이가 4보다 크다면 끝에서부터 4개를 통해 ㄷ을 만든다.
                
또한, DFS 과정 중 해당 노드의 OutDegree (Child 의 수)가 3 개이상이라면 자식 노드 중 3개를 뽑아 ㅈ을 만들 수 있다.
💥 import math => math.comb 는 느리기 때문에 직접 구현해서 사용해야한다.
1) DFS
V, E = 30만이라 DFS 로 충분할 것으로 생각했지만
재귀식이라 시간면에서 불리한 것으로 생각된다.
따라서 시간 복잡도를 더 줄여야한다.

3) Degree
ㅈ을 구하기 위해서 Degree를 이용했는데 이를 ㄷ에도 적용하면 줄일 수 있을 것으로 생각된다.

ㅈ : 한 노드를 기준으로 degree(in & out)가 3이상이라면 그 중 3개를 선택해 ㅈ을 만들 수 있다.

ㄷ : edge 하나를 선택한다면 edge의 양 끝 노드에서 하나씩만 더 뻗어나가면 된다.
    즉 u-v 간선이 있다면 u의 (degree-1) 과 v의 (degree-1) 를 조합하면 ㄷ을 만들 수 있다.
    여기서 degree-1 인 이유는 u-v 선택되었으니 이 값을 제외한 degree 수

이렇게 degree를 이용한다면 O(N) 으로 해결 가능하다.
"""

## 💥 Degree 접근 - Pypy3 통과
n = int(input())
degree = [0] * (n+1)
edges = []
for _ in range(n-1):
    u, v = map(int,input().split())
    degree[u] += 1
    degree[v] += 1
    edges.append([u,v])

D = 0
G = 0
detected = [False] * (n+1)
for edge in edges:
    u, v = edge
    if not detected[u] and degree[u]>=3:
        cnt = degree[u]
        G += ((cnt*(cnt-1)*(cnt-2))//6)
        detected[u] = True
    if not detected[v] and degree[v] >=3:
        cnt = degree[v]
        G += ((cnt*(cnt-1)*(cnt-2))//6)
        detected[v] = True
    
    D += ((degree[u]-1) * (degree[v]-1))
    
if D > G*3:
    print('D')
elif D < G*3:
    print("G")
elif D == G*3:
    print("DUDUDUNGA")




## 💥 DFS 접근  - 오답
# from collections import defaultdict
# import math

# def findRoot(parent):
#     for i in range(len(parent)):
#         if i ==0: continue
#         if parent[i] == -1:
#             return i

# n = int(input())
# graph = defaultdict(list)
# parent = [-1]* (n+1)
# degree = [0] * (n+1)
# for _ in range(n-1):
    # u, v = map(int,input().split())
    # parent[v] = u
    # graph[u].append(v)
    # degree[u] += 1
    # degree[v] += 1

# root = findRoot(parent)
# path = [root]
# visited = [False] * (n+1)
# visited[root] = True
# D = 0
# G = 0


#### DFS 방법은 오답이 된다....??  Only Degree 만으로 접근이 가능하다.
# if degree[root] >= 3:
#     G += math.comb(degree[root], 3)

# def DFS(now, path):
#     global D, G
#     if len(path) >= 4:
#         print(path)
#         D += 1
#     # elif len(path) > 4:
#     #     D += 1
    

    
#     for nxt in graph[now]:
#         if not visited[nxt]:
#             if degree[nxt] >= 3:
#                 G += math.comb(degree[nxt], 3)
            
#             visited[nxt] = True
#             path.append(nxt)
#             DFS(nxt, path)
#             path.pop()


# DFS(root, path)
# if D > G*3:
#     print('D')
# elif D < G*3:
#     print("G")
# elif D == G*3:
#     print("DUDUDUNGA")


