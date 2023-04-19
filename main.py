# -*- coding: utf-8 -*-
"""
Program My Soft base

Created on Tue Apr 19 19:42:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""

import str_common as strc

PATH_TEXT = "docs\\soft_string_save.txt"


def selfdoc():
    print(
        ''' 
           === Any function with JSON on Python ==================================

           def CalcSumNumbers(A):   Рекурс функ - возвращает сумму чисел во входящем наборе
           def Fn(arg, op: str):    Рекурс функ - возвр htpekmnfn {+,-,*} чисел в наборе
           def Test1_recurs(n: int) -> bool:    Тесты
           def Test2_recurs(n: int) -> bool:
           def Test3_recurs(n: int, op: str) -> bool:
           def Test4_recurs(lst: list, op: str) -> bool:
           
           Первая работа: Выясним глубину рекурсии в зависимости от значения cnt
           
           Вторая работа: текст файла разсплитовать и 'множество' слов отсортировать как список"
           
           Третья работа: узнать все об объекте list

           Самодокументируемый текст прораммы не требует подробных комментариев
           
           =======================================================================
        '''
    )

#--- Рекурсивная функция - возвращает сумму чисел во входящем наборе
def CalcSumNumbers(A):
    if A == []:
        # если набор пуст, возвратить 0
        return 0
    else:
        # Вычислить сумму - прибавить первый элемент набора
        summ = CalcSumNumbers(A[1:]) # рекурсивный вызов этой же функции

        # Прибавить к общей сумме первый элемент
        summ = summ + A[0]

        return summ

def Fn(arg, op: str):
    if (arg == []):
        return 0
    else:
        res = Fn(arg[1:], op)
        if (op == "+"):
            res = res + arg[0]
        elif (op == "-"):
            res = res - arg[0]
        elif (op == "*"):
            res = res * arg[0]

        return res


#--- Демонстрация использования функции CalcSumNumbers()
#--- Создать набор чисел разной длины списка и вычислить сумму
def Test1_recurs(n: int) -> bool:
    try:
        L = [x**2 for x in range(0, n)]
        sum = CalcSumNumbers(L)
        #print(sum)
    except:
        print("Err: *** OverRec1 ***")
        return False
    return True

def Test2_recurs(n: int) -> bool:
    try:
        l = [x**2 for x in range(1, n) if x % 2 == 0]
        sum = CalcSumNumbers(l)
        #print(sum)
    except:
        print("Err: *** OverRec2 ***")
        return False
    return True

def Test3_recurs(n: int, op: str) -> bool:
    try:
        l = [x**2 for x in range(1, n)]
        res = Fn(l, op)
    except:
        print("Err: *** OverRec3 ***")
        return False
    return True

def Test4_recurs(lst: list, op: str) -> bool:
    try:
        res = Fn(lst, op)
    except RecursionError:
        print("Err: *** OverRec4 ***")
        return False
    return True

def main():
    print()

    strc.titleprogram("Set of methods with recursia", "Any tests primitive recursion call", "ln.starmark@gmail.com")

    selfdoc()

    strc.zagolovok("Первая работа: Выясним глубину рекурсии в зависимости от значения cnt")

    cnt = 0
    while(Test1_recurs(cnt)):
        cnt += 1
    print(f"Limit1: {cnt}")

    cnt = 0
    while(Test2_recurs(cnt)):
        cnt += 1
    print(f"Limit2: {cnt}")

    cnt = 0
    while(Test3_recurs(cnt, "+")):
        cnt += 1
    print(f"Limit3: {cnt}")

    cnt = 0
    work = True
    while(work):
        l = [x ** 2 for x in range(1, cnt) if x % 2 == 0]
        if(Test4_recurs(l, "*")):
            cnt += 1
        else:
            work = False
    print(f"Limit4: {cnt}")


    strc.zagolovok("Вторая работа: текст файла разсплитовать и 'множество' слов отсортировать как список")
    #--- Зачитать текст из файла, разбить его на слова,
    #--- получить множество из списка неповторных слов
    #--- множество -> снова в список и отсортировать
    with open(PATH_TEXT, "r") as read_file:
        txt = read_file.read()
    print(txt)

    #--- рассплитуем текст
    words = [each_word for each_word in txt.split()]

    #--- создадим множество
    visited = set()
    dup = {el for el in words if el in visited or (visited.add(el) or False)}

    #--- преобразуем в список
    lst = list(dup)

    #--- чтобы отсортировать и распечать по столбцам
    lst.sort()
    strc.Print_table(lst, 12, 10)
    print("\n")

    strc.zagolovok("Третья работа: узнать все об объекте list")
    methods_list = dir(list)
    strc.Print_table(methods_list, 8, 16)
    print("\n")

if __name__ == "__main__":
    main()



