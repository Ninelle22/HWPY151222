#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:


arr = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(arr), 2):
    sum += arr[i]

print(sum)


from random import sample
def random_list(size):
    if size < 0:
        size = -size
    result = sample(range(size), size)
    print(result)
    return result
    
def el_list_sum(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 == 0:
            sum += list[i]
    return sum

print(el_list_sum(random_list(int(input('Enter size of the list: ')))))