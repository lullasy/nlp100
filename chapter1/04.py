#! /usr/bin/env python
# coding:utf-8

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split()

first = [1, 5, 6, 7, 8, 9, 15, 16, 19]
first = map(lambda n:n-1, first)

ret = {}

for i in range(len(str)):
  now = 1 if i in first else 2
  ret[str[i][:now]] = i + 1

print(ret)