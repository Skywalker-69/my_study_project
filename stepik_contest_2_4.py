"""
Самое скучное условие
Зачастую из-за непонятных условий сложно понять суть задачи, поэтому иногда лучше написать коротко и по делу.

Напишите программу, которая находит длину самого длинного палиндрома, который можно составить из букв в строке.

Формат входных данных
На вход программе подается одна строка, состоящая из строчных латинских букв.

Формат выходных данных
Программа должна вывести одно число — длину самого длинного палиндрома, который можно составить из букв в введенной
строке.

Примечание 1. Палиндром читается одинаково в обоих направлениях, например, слово «rotavator».

Примечание 2. Рассмотрим первый тест. Из букв a, b, a, b, q, t, и d можно составить палиндром, например, abqba, длина
 которого равна 55. Палиндром большей длины из данных букв составить нельзя.

Sample Input 1:

ababqtd
Sample Output 1:

5
Sample Input 2:

bebebe
Sample Output 2:

5
Sample Input 3:

qaaaaaaaab
Sample Output 3:

9
"""
line = [i for i in input()]
sum = 0
checked = []
for char in line:
    if char not in checked:
        checked.append(char)
        n = line.count(char) // 2
        if n >= 1:
            sum += n
if len(line) == sum:
    print(sum * 2)
elif len(line) > sum:
    print(sum * 2 + 1)
