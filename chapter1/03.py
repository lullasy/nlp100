#! /usr/bin/env python
# coding:utf-8

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace('.', "")
str = str.replace(',', "")
splitted = str.split()

# print(str)

list = []

for s in splitted:
  list.append(len(s))

print(list)