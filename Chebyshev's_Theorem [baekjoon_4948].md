# 백준 4948번 문제

[1002번: 터렛](https://www.acmicpc.net/problem/4948)

## 코드
```
# checkValue()는 소수인지를 판별하는 함수
# composite number(합성수) :소수가 아니면 True,
# prime number(소수): 소수이면 False
# 1은 소수가 아니다.

import math

def checkValue(numValue):
    if numValue == 1:
        return True
    else:
        # math.sqrt(number) -> number의 제곱근
        # 예: math.sqrt(100) -> 10
        for composite_number in range(2, int(math.sqrt(number)) + 1):
            if numValue % composite_number == 0:
                return False
    return True

# 제한이 1 ≤ n ≤ 123,456이고, 출력을 n보다 크고, 2n보다 작거나 같게 하기 위해
# 2n = 2 * 123456 까지를 range로 정한다.
value = list(range(123456 * 2))
prime_number = list()

for number in value:
    if checkValue(number):
        prime_number.append(number)

# 사용자 입력 및 결과 출력
# 계속 입력 가능~~~~!
while(1):
    insertN = int(input())
    cnt = 0

    if insertN == 0:
        break

    for valueN in prime_number:
        if insertN < valueN <= insertN * 2:
            cnt += 1
    print(cnt)

```

## 예제 입력
<img width="545" alt="베르트랑" src="https://user-images.githubusercontent.com/59908525/145071687-4208c2ab-76e0-410c-a7bf-8393b80fa85d.PNG">

## 예제 풀이
