"""
문제
세준시에는 고층 빌딩이 많다. 세준시의 서민 김지민은 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다. 
빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. 
i번째 빌딩 (1부터 시작)은 (i,0)부터 (i,높이)의 선분으로 나타낼 수 있다. 
고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 
가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 빌딩의 수 N이 주어진다. 
N은 50보다 작거나 같은 자연수이다. 
둘째 줄에 1번 빌딩부터 그 높이가 주어진다. 높이는 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
===============================================================================================================================================
N <= 50 으로 굉장히 적기 때문에 Brute Force로 충분히 해결가능하다.

빌딩 두개를 골라 방정식을 만들고 그 사이에 더 높은 건물이 있다면 보지 못하는 사이이다.
이를 구현하면 된다.
O(N^3) 안에 무조건 해결된다.
"""

from fractions import Fraction
n = int(input())
buildings = [-1] + list(map(int, input().split()))
see = [0]* (n+1)
def equation(x1, y1, x2, y2):
    
    if y1 == y2:
        a = 0
        b = y1
        return a, b
    
    a = Fraction((y1-y2), (x1-x2))
    b = y1 - a * x1
    
    return a, b

for i in range(1, n+1):
    for j in range(i+1, n+1):
        x1, y1, x2, y2 = i, buildings[i], j, buildings[j]
        a, b = equation(x1,y1,x2,y2)
        isSee = True
        for k in range(i+1, j):
            c = a * k + b
            if c <= buildings[k]: ## 보이지 않는다.
                isSee = False
                break
            
        if isSee:
            see[i] += 1
            see[j] += 1
                        
print(max(see))