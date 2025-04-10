"""
Param18. Описать процедуру Chessboard(M, N, A), формирующую по целым
положительным числам M и N матрицу A размера M x N, которая содержит 
числа 0 и 1, расположенные в «шахматном» порядке, причем A[1,1] = 0. 
Двумерный целочисленный массив A является выходным параметром. С помощью 
этой процедуры по данным целым числам M и N сформировать матрицу A 
размера M x N.
Гаврюшкин Максим
11.11.2023
Время: 5 min
"""
def Chessboard(M, N, A):
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            A[i - 1][j - 1] = (i + j) % 2

M = int(input("Vvedite M: "))
N = int(input("Vvedite N: "))

matritsa_custom = [[0 for _ in range(N)] for _ in range(M)]

Chessboard(M, N, matritsa_custom)

print("Rezul'tiruyushchaya matritsa:")
for row in matritsa_custom:
    print(row)
