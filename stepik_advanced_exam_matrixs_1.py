"""
Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется список. Напишите
программу, которая разделяет список на вложенные подсписки так, что nn последовательных элементов принадлежат разным подспискам.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Графическая иллюстрация для 11 теста:

​

Тестовые данные 🟢
Sample Input 1:

a b c d e f g h i j k l m n
3
Sample Output 1:

[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
Sample Input 2:

a b c d e f g h i j k l m n
2
Sample Output 2:

[['a', 'c', 'e', 'g', 'i', 'k', 'm'], ['b', 'd', 'f', 'h', 'j', 'l', 'n']]
Sample Input 3:

a b c d e f g h i j k l m n
1
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']]
"""

list_input = input().split()
n = int(input())
k = 0
if len(list_input) % n != 0:
    k = - 1
list_output = [[] for i in range(n)]
index = 0
flag = True
while flag:
    for j in range(n):
        if index == len(list_input):
            flag = False
            break
        list_output[j].append(list_input[index])
        index += 1
print(list_output[0:n])
