#! /usr/bin/env python
# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: "), next_one
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
# Was hier zu merken ist, wie auch bei einer range() wird die obere Zahl nicht
#mit beachtet. Es wird also nicht der 3., 4. und 5. IndexHalter widergegeben, sondern
# lediglich der 3. und der 4.
