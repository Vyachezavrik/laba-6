#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cоздайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.

if __name__ == '__main__':
    list_1 = {1: 'one', 2: 'two', 10: 'ten', 20: 'twenty', 30: 'thirty', 50: 'fifty'}
    list_2 = dict(map(reversed, list_1.items()))

    print(list_1)
    print(list_2)