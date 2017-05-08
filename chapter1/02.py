#! /usr/bin/env python
# coding:utf-8

str1 = "パトカー"
str2 = "タクシー"
str3 = ""

for s1, s2 in zip(str1, str2):
  str3 += (s1 + s2)

print(str3)