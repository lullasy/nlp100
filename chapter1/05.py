#! /usr/bin/env python
# coding:utf-8

def bi_gram(words):
  ret = []
  for i in range(0, len(words)):
    ret.append(words[i:i + 2])

  return ret

str = "I am an NLPer"
print(bi_gram(str))
print(bi_gram(str.split(' ')))