"""
문제 출처 : https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
※ SW expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

  게으름뱅이 왕국에는 N명의 게으른 사람들이 있다. 오늘 왕국에는 K개의 중요한 일이 있다. 
  모든 일은 한 사람이 맡아야 하고, 한 사람은 많아야 하나의 일을 할 수 있다. 
  왕은 각 사람들이 하고 싶은 일을 고르게 했고, i번 사람은 ai번 일을 골랐다.
  하지만, 몇 개의 일은 아무도 선택하지 않았을 수 있어서, 왕은 이들에게 선택되지 않은 일을 고르라고 설득해야 한다. 
  왕은 i번째 사람이 자신이 원하는 일을 하도록 설득하는 데 bi시간이 걸린다는 것을 알고 있다.
  모든 K개의 일이 진행되기 위해, 왕이 써야 하는 필요한 최소 시간 합은 얼마인가?

[입력]
  첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 
  각 테스트 케이스는 다음과 같이 구성되었다.
  첫 번째 줄에 정수 N, K가 주어진다. (1 ≤ K ≤ N ≤ 105)
  두 번째 줄에 N개의 정수로 i번째 사람이 고른 일 ai가 주어진다. (1 ≤ ai ≤ K)
  세 번째 줄에 N개의 정수로 i번째 사람을 설득하기 위해 필요한 시간 bi 가 주어진다. (1 ≤ bi ≤ 109)

[출력]
  각 테스트 케이스 마다 한 줄씩 문제의 정답을 출력하라.
=======================================================================================================================================
💥 How to Solve?
- 한 사람만 원하는 일은 바로 배당한다.
- 여러 사람이 원하는 일인 경우 가장 설득하기 어려운 사람을 배당한다. => 설득하는 시간이 가장 큰 사람을 배당한다.
- 남은 사람들 중 설득하기 쉬운 순서대로 남은 업무를 배당한다. => 이 때, 설득하는 시간이 발생한다.
"""


def who_hold_work(peoples, time):
    max_people = [-1, -1]
    for p in peoples:
        max_people = [p, time[p]] if time[p] > max_people[1] else max_people
    
    return max_people
T = int(input())
for t in range(1, T+1):
    
    N, K = map(int, input().split())
    
    work = [-1] + list(map(int, input().split()))
    time = [-1] + list(map(int, input().split()))
    
    people_work = {i:[] for i in range(1, K+1)}
    for i in range(1, N+1):
        people_work[work[i]].append(i)
    
    finish = 0
    popular_work = []
    for k,v in people_work.items():
        if len(v) == 1:
            finish += 1
        elif len(v) > 1:
            popular_work.append(k)

    
    any_work_people = []
    
    for p in popular_work:
        candidate = people_work[p]
        m = who_hold_work(candidate, time)
        finish +=1
        candidate.remove(m[0])
        any_work_people += candidate
    
    
    p_w = {i : time[i] for i in any_work_people}

    p_w = sorted(p_w.items(), key = lambda x: x[1])
    res = 0
    for e, v in enumerate(p_w):
        if e+1 > K- finish:
            break
        res += v[1]
    
    print('#{} {}'.format(t, res))
    
    


