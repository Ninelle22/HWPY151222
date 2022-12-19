#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

s = ''
n = int(input())
while n > 0:
    s += str(n % 2)
    n //=2
    print(s[::-1])

s = ''
n = int(input())
while n > 0:
    s += str(n % 2)
    # s = str(n % 2) + s
    n //= 2
print(s[::-1])



def decimal_digit_to_binery(num):
    if num == 0:
        print(num)
        return
    elif num != 1:
        decimal_digit_to_binery(num // 2)
    print(num % 2, end='')
    
decimal_digit_to_binery(int(input('Enter decimal number:  ')))
print()