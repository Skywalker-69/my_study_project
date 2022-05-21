"""
Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.

Тестовые данные 🟢
Sample Input 1:

3
4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
Sample Output 1:

12 11 13 14
22 21 23 24
32 31 33 34
Sample Input 2:

3
3
11 12 13
21 22 23
31 32 33
2 1
Sample Output 2:

11 13 12
21 23 22
31 33 32
Sample Input 3:

3
5
12 14 11 13 24
22 24 21 23 14
32 34 31 33 34
0 2
Sample Output 3:

11 14 12 13 24
21 24 22 23 14
31 34 32 33 34
"""

n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    matrix.append([int(num) for num in input().split()])
change = [int(num) for num in input().split()]
first_column, second_column = change[0], change[1]

for i in range(n):
    matrix[i][first_column], matrix[i][second_column] = matrix[i][second_column], matrix[i][first_column]

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=" ")
    print()
