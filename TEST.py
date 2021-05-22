""" 이건 하트!!!
예 :
>>> 365
------
♥♥♥
♥♥♥♥♥♥
♥♥♥♥♥ """

import time

def print_sleep(print, sleep):
    print(print)
    sleep(sleep)
    return

number_st = input('숫자')
number2 = 1
list_1 = []
len_1 = len(number_st)

for i in range(len_1):
    a = number_st[number2 - 1: number2]
    a = int(a)
    list_1.append(a)
    number2 += 1
number3 = 1
string = ''
for i in range(len_1):
    string = ''
    for j in range(list_1[i]):
        string = string + '♥'
    print(string)
    time.sleep(0.3)

number_st = input('숫자')
for i in number_st:
    for j in range(int(i)):
        print('♥', end='')
    time.sleep(0.3)
    print()


a = 1
b = 1



def multiplication():
    global a
    global b
    print(b, '*', a, '=', b * a)
    a += 1


for i in range(9):
    for e in range(9):
        multiplication()
    a = 1
    b += 1
