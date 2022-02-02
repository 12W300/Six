#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    def decorator(fn):
        def wrapper(st1, st2):
            print(st1)
            print(st2)
            arrkey, arrval = fn(st1, st2)
            return dict(zip(arrkey, arrval))
        return wrapper


@decorator
def str_to_list(s1, s2):
    lst1 = list(s1.split())
    lst2 = list(s2.split())
    return lst1, lst2


str1 = 'key1 key2 key3 key4 key5'
str2 = 'val1 val2 val3 val4 val5'

print(str_to_list(str1, str2))
