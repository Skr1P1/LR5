#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# В списке, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента списка;------
# 2) сумму модулей элементов списка, расположенных после первого отрицательного элемента.
# 3)Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

import math
from random import random

if __name__ == '__main__':
    # номер минимального по модулю элемента списка
    m = float
    u = list(map(float, input('Введите вещественные числа -->').split()))
    for i in u:
        if abs(i) < abs(min(u)):
            m = i
    print(m)
    for i in u:
        if i < 0:
            break
    # сумму модулей элементов списка, расположенных после первого отрицательного элемента
    s = 0
    neg = -1
    for i, n in enumerate(u):
        if n < 0:
            neg = i
            break

    for n in u[neg + 1:]:
        s += abs(n)

    print(s)

    # Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].
    N = 10
    a = []
    l = float(input('Нижняя граница массива: '))
    h = float(input('Верхняя граница массива: '))
    for i in range(N):
        n = float(random() * (h - l)) + l
        a.append(n)
    print(a)
    print('Удаляемый диапазон')
    l = float(input('нижняя граница: '))
    h = float(input('верхняя граница: '))
    i = 0
    m = N
    while i < m:
        if l <= a[i] <= h:
            del a[i]
            m -= 1
        else:
            i += 1
    for i in range(m, N):
        a.append(0)
    print(a)

