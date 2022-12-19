#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


arr  = [1.1, 1.2, 3.1, 5, 10.01]
arr = [x for x in arr if type(x) == float]
arr_float = list()
for i in arr:
    arr_float.append(round(i % 1, 5))
print(max(arr_float) - min(arr_float))





import random as r

def getList(size):
    if size < 0:
        size = -size
    result = [0.0] * size
    for i in range(size):
        result[i] = round(r.uniform(0, 1000), 2)
    print(result)
    return result

def minMax(List):
    min = List[0] - List[0] // 1
    max = min
    for i in range(len(List)):
        fract = List[i] - List[i] // 1
    if fract > max:
        max = fract
    if fract < min:
        min = fract
    print(f'Min fraction part:{round(min, 2)}\n', f'Max fraction part: {round(max, 2)}\n',end='')
    return round(max-min, 2)
        
print('Diff: ', minMax(getList(int(input('Enter the size of the List: ')))))