#!/usr/bin/env python3

import ipdb

def happy_new_year():
    x = 0
    while x <= 9:
        print(10 - x)
        x += 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    all_squares = [integer * integer for integer in int_list]
    return all_squares
    pass

def fizzbuzz():
    for x in range(1, 101):
      if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
      elif x % 3 == 0:
        print("Fizz")
      elif x % 5 == 0:
        print("Buzz")
      else:
        print(x)
    pass

fizzbuzz()