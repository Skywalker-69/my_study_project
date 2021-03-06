"""
Побочная диагональ
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и
заполняет её по следующему правилу:

числа на побочной диагонали равны 11;
числа, стоящие выше этой диагонали, равны 00;
числа, стоящие ниже этой диагонали, равны 22.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ — это диагональ, идущая из правого верхнего в левый нижний угол матрицы.

Тестовые данные 🟢
Sample Input 1:

4
Sample Output 1:

0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
Sample Input 2:

2
Sample Output 2:

0 1
1 2
Sample Input 3:

3
Sample Output 3:

0 0 1
0 1 2
1 2 2
"""

n = int(input())

matrix = []
for _ in range(n):
    matrix.append([0 for _ in range(n)])

for r in range(n):
    for c in range(n):
        if r + c + 1 == n:
            matrix[r][c] = 1
        elif r < c and r > n - 1 - c:
            matrix[r][c] = 2
        elif r > c and r > n - 1 - c:
            matrix[r][c] = 2
        elif r >= n // 2 and c >= n // 2:
            matrix[r][c] = 2
for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
