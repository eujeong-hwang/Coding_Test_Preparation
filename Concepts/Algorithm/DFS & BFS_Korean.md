# DFS & BFS의 설명과 차이점

DFS(깊이 우선 탐색) 와 BFS(너비 우선 탐색)은 그래프를 탐색하는 방법이다. <br/>

# 그래프란? 
Node(정점)과 그 정점을 연결하는 Edge(간선)으로 이루어진 자료구조의 일종이며, 
그래프를 탐색한다는 것은 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것을 말한다. <br/>


# 그래프와 트리의 차이
<img width="560" alt="그래프와 트리의 차이" src="https://user-images.githubusercontent.com/59908525/146516938-6e24045d-f153-4866-baf4-76288c57dfa7.PNG">


# Depth-First Search (DFS): 깊이 우선 탐색

![R1280x0](https://user-images.githubusercontent.com/59908525/146517324-ea67966c-090c-468f-b5f6-476b36e68e67.gif)

출처 : https://developer-mac.tistory.com/64 

<br>

- 최대한 깊이 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우, 옆으로 이동하는 방법이다. 
- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식을 말합니다.

<br>

# When do we use DFS?

1. 모든 노드를 방문하고자 하는 경우.
2. DFS이 BFS보다 좀 더 간단하다.
3. 검색 속도 자체는 BFS 보다 느리다.

<br>

# Breadth-First Search (BFS) : 너비 우선 탐색

![R1280x0-4](https://user-images.githubusercontent.com/59908525/146521771-3c3f50e2-04c4-4e2d-bef8-58ae30fa1856.gif)

출처 : https://developer-mac.tistory.com/64 

- 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동
- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로,
시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법입니다.

<br>

# When do we use BFS?

1. 주로 두 노드 사이의 최단 경로를 찾고 싶을 때 이 방법을 선택.

<br>

# DFS와 BFS의 차이점
![R1280x0-3](https://user-images.githubusercontent.com/59908525/146522217-0373fb29-74f7-4ada-b516-8fd9e4bed034.gif) <br/>

<img width="800" alt="캡처" src="https://user-images.githubusercontent.com/59908525/146522221-9e083ce7-093d-4d6a-87e4-ffc1bb30eec4.PNG">

# 시간 복잡도

두 방식 모두 조건 내의 모든 노드를 검색한다는 점에서 시간 복잡도는 동일합니다.
DFS와 BFS 둘 다 다음 노드가 방문하였는지를 확인하는 시간과 각 노드를 방문하는 시간을 합하면 됩니다.

<br>

# 푸는 방법

1. DFS

- 첫 번째로 스택을 이용하는 것

- 두 번째로 재귀함수를재귀 함수를 이용하는 것인데, 재귀 함수를 이용하는 것이 가장 보편적이고 짧은 코드를 작성할 수 있다.

2. BFS

- BFS 알고리즘은 큐(Queue)를 사용해서 문제를 해결하면 됩니다.

# Reference
https://devuna.tistory.com/32 <br/>
https://velog.io/@lucky-korma/DFS-BFS%EC%9D%98-%EC%84%A4%EB%AA%85-%EC%B0%A8%EC%9D%B4%EC%A0%90