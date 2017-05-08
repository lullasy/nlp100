#! /usr/bin/env python
# coding:utf-8

def cipher(str):
  ret = ""
  for c in str:
    if c.islower():
      c = chr(219 - ord(c))
    ret += c
  return ret

test = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(cipher(test))