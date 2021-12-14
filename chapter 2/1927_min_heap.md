# 백준 1927번 문제

[1927번: Min Heap](https://www.acmicpc.net/problem/1927)

## 코드
```
import heapq
import sys

# 연산의 개수 N
N = int(input())

# heap이라는 배열 생성
heap = []

# 만약 x가 자연수라면 배열에 추가
# x == 0이면 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 삭제
for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        # heap 배열에 값이 있다면, heappop()[1]를 출력하고
        if heap:
            print(heapq.heappop(heap))
        # heap이 비어있다면, 0을 출력
        else:
            print("0")
    else:
        heapq.heappush(heap, x)

```
