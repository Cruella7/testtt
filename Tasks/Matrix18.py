"""
Matrix18. Дана матрица размера M * N и целое число K (1 <= K <= N).
Найти сумму и произведение элементов K-го столбца данной матрицы.
Гаврюшкин Максим
11.11.2023
Время: 10 min
"""
def sum_and_product(matrix, k):
    if 1 <= k <= len(matrix[0]):
        column = [row[k - 1] for row in matrix]
        column_sum = sum(column)
        column_product = 1
        for element in column:
            column_product *= element
        return column_sum, column_product
    else:
        return "Ошибка"


M = int(input("M: "))
N = int(input("N: "))

matrix = []
for i in range(M):
    row = [int(input(f"Введите элемент матрицы ({i+1}, {j+1}): ")) for j in range(N)]
    matrix.append(row)

K = int(input("Введите номер столбца K: "))

result = sum_and_product(matrix, K)

if type(result) == tuple:
    column_sum, column_product = result
    print(f"Сумма элементов {K}-го столбца: {column_sum}")
    print(f"Произведение элементов {K}-го столбца: {column_product}")
else:
    print(result)
