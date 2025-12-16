#Python Basic Exercise for Beginner

Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

With given input
"""

number1 = 20
number2 = 30
product = number1 * number2
sum = number1 + number2

if product <= 1000:
  print("product :",product)
else:
  print("sum: ", sum)

"""Input by User"""

number1 = int(input("input 1st number:"))
number2 = int(input("input 2nd number:"))
product = number1 * number2
sum = number1 + number2

if product <= 1000:
  print("product:",product)
else:
  print("sum:",sum)

avg = (number1 + number2) / 2
print("average:", avg)

"""Using Function"""

def multiplication_or_sum(num1, num2):
  product = num1 * num2

  if product <= 1000:
    return product
  else:
    return num1 + num2

def average(num1,num2):
  return (num1 + num2)/2

number1 = int(input("number1:"))
number2 = int(input("number2:"))


result = multiplication_or_sum(number1,number2)
print("The result is", result)

avg = average(number1, number2)
print("The average is", avg)