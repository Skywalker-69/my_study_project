"""
Ходы ферзя
На шахматной доске 8 \times 88×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
 Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки
 заполните точками.

Формат входных данных
На вход программе подаются координаты ферзя на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
записывается номер столбца (буква от a до h, слева направо), затем номер строки (цифра от 11 до 88, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

Тестовые данные 🟢
Sample Input 1:

c4
Sample Output 1:

. . * . . . * .
. . * . . * . .
* . * . * . . .
. * * * . . . .
* * Q * * * * *
. * * * . . . .
* . * . * . . .
. . * . . * . .
Sample Input 2:

a1
Sample Output 2:

* . . . . . . *
* . . . . . * .
* . . . . * . .
* . . . * . . .
* . . * . . . .
* . * . . . . .
* * . . . . . .
Q * * * * * * *
Sample Input 3:

h5
Sample Output 3:

. . . . * . . *
. . . . . * . *
. . . . . . * *
* * * * * * * Q
. . . . . . * *
. . . . . * . *
. . . . * . . *
. . . * . . . *
"""
coordinates = input()
alphabet = 'abcdefgh'
numbers = '87654321'
column = alphabet.find(coordinates[0])
row = numbers.find(coordinates[1])
print(column, row)
matrix = []
for _ in range(8):
    matrix.append(['.' for _ in range(8)])
for i in range(8):
    for j in range(8):
        if j == column and i == row:
            matrix[i][j] = 'Q'
        elif i == row:
            matrix[i][j] = '*'
        elif j == column:
            matrix[i][j] = '*'
        elif j - i == column - row:
            matrix[i][j] = '*'
        elif j + i == column + row:
            matrix[i][j] = '*'

for r in range(8):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()
