# 이진 트리에서 임의의 두 정점의 공통 조상 중 가장 가까운 것을 찾으려 한다.
# 예를 들어, 아래의 이진 트리에서 정점 8과 13의 공통 조상은 정점 3와 1 두 개가 있다.
# 이 중 8, 13에 가장 가까운 것은 정점 3이다.
# 정점 3을 루트로 하는 서브 트리의 크기(서브 트리에 포함된 정점의 수)는 8이다.
# 임의의 이진 트리가 주어지고, 두 정점이 명시될 때 이들의 공통 조상 중 이들에 가장 가까운 정점을 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하라.
# 입력에서 주어지는 두 정점이 서로 조상과 자손 관계인 경우는 없다.
# 위의 트리에서 예를 든다면 두 정점이 “11과 3”과 같이 주어지는 경우는 없다.
# [입력]
# 가장 첫줄은 전체 테스트케이스의 수이다.
# 10개의 테스트 케이스가 주어진다.
# 두 줄이 하나의 테스트 케이스가 되며, 따라서 전체 입력은 20줄로 이루어진다.
# 각 케이스의 첫줄에는 트리의 정점의 총 수 V와 간선의 총 수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어진다 (정점의 수 V는 10 ≤ V ≤ 10000 이다). 
# 그 다음 줄에는 E개 간선이 나열된다. 간선은 간선을 이루는 두 정점으로, 항상 “부모 자식” 순서로 표기된다.
# 위에서 예로 든 트리에서 정점 5와 8을 잇는 간선은 “5 8”로 표기되고, 절대로 “8 5”와 같이 표기되지는 않는다.
# 간선이 입력되는 순서는 정해져 있지 않다. 입력에서 이웃한 수는 모두 공백으로 구분된다.
# 정점의 번호는 1부터 V까지의 정수이며, 전체 트리에서 루트가 되는 정점은 항상 1번으로 표기된다.
# 부모 정점이 자식 정점보다 항상 번호가 작은 것은 아니다. 즉, 40번 정점이 20번 정점의 부모가 될 수도 있다.
# 이 문제에서 자식 정점이 부모 정점의 왼쪽 자식인지 오른쪽 자식인지는 중요하지 않다.
# [출력]
# 총 10줄에 10개의 테스트 케이스 각각에 대한 답을 출력한다.
# 각 줄은 테스트 케이스의 번호를 의미하는 ‘#x’로 시작하고 공백을 하나 둔 다음 답을 기록한다.
# 답은 공통조상 중 가장 가까운 것의 번호, 그것을 루트로 하는 서브 트리의 크기를 뜻하는 2개의 정수로 구성된다. 이 두 정수는 공백으로 구분한다.

import sys
sys.stdin = open('input.txt')


def find(x):
    if 1 != parent[x]:
        mom.append(parent[x])
        find(parent[x])
    else:
        mom.append(parent[x])
        return

def subtree(x,goal):
    global cnt
    if goal == parent[x]:
        cnt += 1
        return
    elif x == parent[x]:
        return
    else:
        subtree(parent[x],goal)


for tc in range(int(input())):
    print('#{}'.format(tc+1), end=' ')
    node,path,i,you = map(int,input().split())
    datas = list(map(int,input().split()))

    parent = [1]*(node+1)
    son = [0]*(node-1)
    for idx in range(len(datas)//2):
        parent[datas[2*idx+1]] = datas[2*idx]
        son[idx] = datas[2*idx+1]
    # print(parent)
    # print(son)

    mom = []
    find(i)
    i_mom = mom[:]
    mom = []
    find(you)
    you_mom = mom[:]
    # print(i_mom)
    # print(you_mom)

    for target in i_mom:
        if target in you_mom:
            same = target
            break
    print(same, end=' ')

    cnt = 0
    for target in son:
        subtree(target,same)
    print(cnt+1)


