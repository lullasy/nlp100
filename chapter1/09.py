#! /usr/bin/env python
# coding:utf-8

import random

def word_rand(words):
  ret = []
  for word in words:
    if len(word) <= 4:
      ret.append(word)
      continue
    s = word[1:-2]
    s = ''.join(random.sample(s, len(s)))
    s = word[0] + s + word[-1]
    ret.append(s)

  return ret

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(' '.join(word_rand(str.split(' '))))