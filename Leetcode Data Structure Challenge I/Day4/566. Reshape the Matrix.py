# https://leetcode.com/problems/reshape-the-matrix/

# 이건 문제부터 이해 안되서 유튜브 봄...이번주에 한거 다 이해+풀이 다 외워버려야지 ㅜ..ㅜ..심각하다 유정아ㅜ.ㅜ
# https://www.youtube.com/watch?v=24DvdE-XP5E -> 왜 이분이 문제 읽어주시니깐 이해가 되지 ㅋㅋㅋㅋ
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N, M = len(mat[0]), len(mat)
        T = r*c

        if N*M != T:
            return mat
        
        output = [[0 for _ in range(c)] for _ in range(r)]
        temp = []
        for i in range(M):
            for j in range(N):
                temp.append(mat[i][j])
        k = 0
        for i in range(r):
            for j in range(c):
                output[i][j] = temp[k]
                k += 1
        return output