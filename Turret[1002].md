# 백준 1002번 문제

[1002번: 터렛](https://www.acmicpc.net/problem/1002)

## 코드

```
import math

n = int(input())

# underscore(_) can be used as a varaible in looping
for _ in range(n):
    # map() : 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용.
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2: # 두 원의 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0) 
```

## 예제 입력
<img width="900" alt="turret예제" src="https://user-images.githubusercontent.com/59908525/145014725-aee4c831-2cfb-4a4a-ae16-46f45f58801b.PNG">

## 예제 풀이

#### x1: 0, x2: 0, r1: 13, y1: 40, y2: 0, r2: 37 인 경우
![KakaoTalk_20211207_193030521](https://user-images.githubusercontent.com/59908525/145014551-ad2ea01e-9288-4d85-827d-2b01aa8117f2.jpg)

#### x1: 0, x2: 0, r1: 3, y1: 0, y2: 7, r2: 4 인 경우
![KakaoTalk_20211207_193030521_01](https://user-images.githubusercontent.com/59908525/145014557-c6815c24-912c-413e-8804-b9644668c5a7.jpg)

#### x1: 1, x2: 1, r1: 1, y1: 1, y2: 1, r2: 5 인 경우
![KakaoTalk_20211207_193030521_02](https://user-images.githubusercontent.com/59908525/145014567-952f9773-0e56-4a62-baf7-e79d1232c2a3.jpg)
