#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

    
arr = [2, 3, 4, 5, 6]
len_list = 0
if len(arr) % 2 == 0:
    len_list = len(arr) // 2
else:
    len_list = len(arr) // 2 + 1


arr = [2, 3, 4, 5, 6]
for i in range(len_list):
    print(arr[i] * arr[len(arr) - i -1])

 
for i in range((len(arr) +1) // 2):
    print(arr[i] * arr[len(arr) - i -1])


from random import sample as sam

def SumList(List):
    sum = [0]
    for i in range(len(List) // 2):
        sum.append(List[i]*List[len(List) - i - 1])
    if not len(List) % 2 == 0:
        sum.append(List[len(List) - len(List) // 2 - 1])
        sum.remove(0)
        return sum
    
digits = list(sam(range(5), 5))
print(digits)
print(SumList(digits))
