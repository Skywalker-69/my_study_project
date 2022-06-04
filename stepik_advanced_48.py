"""
Страны и города
На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу,
которая для каждого города выводит, в какой стране он находится.

Формат входных данных
Программа получает на вход количество стран nn. Далее идет nn строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число mm, далее идут mm запросов — названия
каких-то mm городов, из перечисленных выше.

Формат выходных данных
Программа должна вывести название страны, в которой находится данный город в соответствии с примером.

Тестовые данные 🟢
Sample Input:

2
Германия Берлин Мюнхен Гамбург Дортмунд
Нидерланды Амстердам Гаага Роттердам Алкмар
4
Амстердам
Алкмар
Гамбург
Гаага
Sample Output:

Нидерланды
Нидерланды
Германия
Нидерланды
"""
n = int(input())
list_input = []
for _ in range(n):
    list_input.append([item for item in input().split()])
dict_cities = {}
for item in list_input:
    dict_cities[item[0]] = item[1:]
m = int(input())
for _ in range(m):
    city = input()
    for key, value in dict_cities.items():
        if city in value:
            print(key)
