#! /usr/bin/env python
# coding:utf-8

def bi_gram(words):
  ret = []
  for i in range(0, len(words) - 1):
    ret.append(words[i:i + 2])

  return ret

str1 = "paraparaparadise"
str2 = "paragraph"

str1 = set(bi_gram(str1))
str2 = set(bi_gram(str2))

print(str1)
print(str2)

print("和集合" + str((str1 | str2)))
print("差集合" + str((str1 - str2)))
print("積集合" + str((str1 & str2)))

search = "se"

print("X : " + str((search in str1)))
print("Y : " + str((search in str2)))
