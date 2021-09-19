# # 하노이 탑 이동 순서
# 첫 번째 n개의 원판 - 반경이 큰 순서대로
# 첫 번째 장대에서 세 번째 장대로 옮겨야한다.

# 한 번에 한 개의 원판만 이동 가능
# 원판은 항상 위의 것이 아래의 것보다 작아야함.
# 최소 이동 횟수는?


# 몇 단인지에 따라서 
# 2의 제곱순으로 이동을 한다 
# 즉 만약 3단이라면

# 1
# 2
# 3
# 일때 1은 2^(3-1) 만큼 즉 4번 이동
# 2는 2^(2-1) 즉 2번 이동
# 3은 2^(1-1) 즉 1번 이동
# 총 7번 이동

# 재귀적으로 판단하는 것은
# 아래와 같다

# 맨 아래를 3번 기둥에 옮기기 위해서는 
# 1~4번이 차례대로 2번에 쌓여있어야 한다.
# 여기에서 4번이 2번 맨 아래에 있기 위해서는 
# 다시 한번 1~3번이 3번 기둥에 있어야한다.
# 이런식으로 쭉
# 3번이 3번 기둥에 있기 위해서는 1~2번이  2번 기둥으로
# ...

def hanoi(N, start, destination, other):
    if N == 0:
        return
    
    hanoi(N-1, start, other, destination)
    print("{0} {1}".format(start, destination))
    hanoi(N-1, other, destination, start)

N = int(input())
cnt = 0
for i in range(N):
    cnt += 2**(i)
print(cnt)
hanoi(N, 1,3,2)