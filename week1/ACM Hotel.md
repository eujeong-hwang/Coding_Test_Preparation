# 백준 10250번 문제

[1002번: ACM 호텔](https://www.acmicpc.net/problem/10250)

## 코드
```
t = int(input())

for i in range(t):
    # h: 각 층 수, w: 각 방의 수, n: 몇 번째 손님
    h, w, n = map(int, input().split())
    floor = n % h
    room = n//h+1

    if floor == 0:  #만약 꼭대기 층일 경우
        floor = h
        room -= 1
    print(floor*100 + room)

```

## 예제 입력
<img width="900" alt="ACM예제" src="https://user-images.githubusercontent.com/59908525/145070962-17b1a421-51c5-48e9-86a6-19ba2693e267.PNG">

## 예제 풀이
