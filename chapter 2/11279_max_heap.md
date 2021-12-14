# 백준 11279번 문제

[11279번: Max Heap](https://www.acmicpc.net/problem/11279)

## 코드
```
# 연산의 개수 N
N = int(input())

# heap이라는 배열 생성
heap = []

# 만약 x가 자연수라면 배열에 추가
# x == 0이면 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 삭제
for i in range(N):
    x = int(sys.stdin.readline())
    # b = x * -1

    if x == 0:
        # heap 배열에 값이 있다면, heappop()[1]를 출력하고
        if heap:
            print(heapq.heappop(heap)[1])
            # print(heapq.heappop(heap)*-1)
        # heap이 비어있다면, 0을 출력력
        else:
            print("0")
    else:
        # heapq.heappush(heap, [-x, x])
        heapq.heappush(heap, b)
```
[-x, x]를 한 이유는, heapq 모듈이 기본적으로 min-heap 형태로 동작함.
그렇기 때문에, -x를 넣어서 가장 작은 값이 되어서 root node에 가도록 설정 !
pop을 할 때, heapq.heappop(heap)[1]를 반환하는 이유는 -x가 아닌, x를 반환하기 위해서
