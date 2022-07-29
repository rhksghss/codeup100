"""
2022-07-29 횬다이 누가바 해몽

# 2
문제)
- i와 i*2, i*2+1 두 정점 사이 간선이 있다.
- Q개의 질문 (Q<=1만)
- 각 Q마다 정점 S, T를 입력받는다. (S,T<=만)
- S와 T의 최단 거리를 구해야한다.

sol)
- heap 풀이
- 문제가 원하는 그래프를 살펴보면 Full binary tree 구조임을 알 수 있다.
- 두 정점사이의 거리를 어떻게 계산하느냐
- 두 정점 사이를 계산하는 경우들을 관찰해본다.

- LCA (최단경로의 반환점)(Lowest Common Ancestor)
- 한 정점의 조상들이랑, 다른 정점의 조상들이랑 가장 낮은 위치에서 겹치는 경우 반환점이 된다.
- (S의 조상) 교집합 (T의 조상) 중 제일 아래있는 점 => 반환점

- 관찰 특성!!!
- 0: 왼쪽, 1: 오른쪽 이라고 하자!
- 13은 2진수로 표현하면 1101(2)
- 첫 번째 1은 무시하고 두번째부터 보면 오왼오

- 10은 이진수로 표현하면 1010(2)
- 동일하게 첫번째 1은 무시하고 두번째부터 보면 왼오왼

- 9 => 1001(2) 왼왼오

=> 루트노드에서 이 순서대로 이동하면 해당 값으로 도착

이런 특성이 어떻게 풀이에쓰이느냐

마지막 공통조상에서 부터의 깊이의 합이 최단거리가 된다.

마지막 공통조상은 갈라지는 부분이 공통조상이 된다.

S와 T를 이진수로 표현하면
S: 111 0(2) 오오왼
T: 111 1(2) 오오오

공통된 점 이후의 남은 길이의 합이 최단 거리가 된다
=> 1+1 =2

S에서 반환점을 왔다가 T로가는 거리 = 반환점에서 S로 가는 거리 + 반환점에서 T로 가는 거리

ex)
S: 11010 01110
T: 11010 11
=> 5+2=7

이렇게 풀거나 실제로 조상들을 다 구해서 문제를 풀어도 된다. 하지만, 이렇게 풀면 더 재밌으니까.. ㅎ


"""


import sys
si = sys.stdin.readline
Q = int(si())
for _ in range(Q):
    S, T = map(int, si().split())
    S = bin(S)
    T = bin(T)
    i = 0
    while True:
        if i == len(S) or i == len(T):
            break
        if S[i] != T[i]:
            break
        i += 1

    print(len(S) - i + len(T) - i)









