#! /usr/bin/env python
# -*- coding: utf-8 -*-
def whileLoop(n, x):
    i = 0
    numbers = []

    for i in range(0, n):
        print("At the top i is %d" % i)
        numbers.append(i)

        i += x
        print("Numbers now: ", numbers)
        print("At the bottum i is %d" % i)

    print("The Numbers: ")

    for num in numbers:
        print num

whileLoop(input(),input())
