#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

if __name__ == '__main__':
    school = {'1a': 25, '1б': 20,
              '2а': 15, '2б': 17,
              '3а': 14, '3б': 18,
              '4а': 10, '4б': 11,
              '5а': 11, '5б': 9,
              '6а': 15, '6б': 17,
              '7а': 12, '7б': 13,
              '8а': 20, '8б': 21,
              '9a': 19, '9б': 30,
              '10a': 15, '10б': 10,
              '11a': 9, '11б': 6
              }
    print(school)

    school['5б'] += 3
    school['9в'] = 10
    school.pop('5б', 9)

    sum1 = 0
    for item in school.values():
        sum1 += item
    print(school)
    print("Количество учеников во всех классах: ", sum1)