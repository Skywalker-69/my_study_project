"""
NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. Суть этого кодирования в том, что имея некоторое устройство,
имеющее всего два состояния, мы строим диаграмму его состояний на каждом такте, и если состояние изменилось, то это расценивается как двоичная единица,
 если же состояние осталось неизменным, то записывается двоичный ноль.

Напишите программу, которая переводит NRZI код в двоичный.

Формат входных данных
На вход программе подается строка, содержащая NRZI код, составленный из символов _, ‾ и |. Длина строки не превышает 85000 символов.

Формат выходных данных
Программа должна преобразовать введенный NRZI код в двоичный код и вывести полученный результат.

Примечание 1. Обозначения:

_ – первое состояние устройства;
‾ – второе состояние устройства;
| – переключение устройства в другое состояние.

Sample Input 1:

_|¯|____|¯|__|¯¯¯
Sample Output 1:

011000110100
Sample Input 2:

|¯|___|¯
Sample Output 2:

11001
Sample Input 3:

________________________________________________________________________________________
Sample Output 3:

0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
"""


def change_code(nrzi_code):
    counter = 0
    output_twin_code = ''
    for i in range(0, len(nrzi_code)):
        if i + counter == len(nrzi_code):
            return output_twin_code
        else:
            if nrzi_code[i + counter] == '|':
                output_twin_code += '1'
                counter += 1
            else:
                output_twin_code += '0'
    return output_twin_code


print(change_code('_|¯|____|¯|__|¯¯¯'))  # 011000110100
print(change_code('|¯|___|¯'))  # 11001
print(change_code('________________________________________________________________________________________'))
# 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000