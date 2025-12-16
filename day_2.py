#Exercise 2
#Print the Sum of a Current Number and a Previous Number
#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

def prev_num(num):
    if num == 0:
        return 0
    else:
        return num - 1

previous_sum =0
print("Printing current and previous number sum in a range(10)")
for i in range(10):
  previous_sum = prev_num(i) + i
  
  print("Current number", i, "Previous number", prev_num(i), "Sum:", previous_sum)

#Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

string = str(input("Original String is:" ))
print("Original string is", string)
print("Printing only even index chars")

for i in range(len(string)):
  if i % 2 == 0:
    print(string[i])

#Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word, n):
      return word[n:]

print("Removing characters from a string")
print(remove_chars("pynative", 4))

print(remove_chars("pynative", 2))

#Exercise 5: Check if the first and last numbers of a list are the same

#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check_list(num):
  if num[0] == num[len(num)-1]:
    return True
  else:
    return False

print(check_list(numbers_x))
print(check_list(numbers_y))

#Exercise 6: Display numbers divisible by 5

#Write a Python code to display numbers from a list divisible by 5

number = [10, 20, 33, 46, 55, 35]

for i in range(len(number)):
  if number[i] % 5 == 0:
    print(number[i])


#Exercise 7: Find the number of occurrences of a substring in a string

#Write a Python code to find how often the substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer."

x = str_x.count("Emma")

print("Emma appeared",x, "times")

#Exercise 8: Print the following pattern

rows = 7

for i in range(rows + 1):
  for j in range(i):
    #display number
    print(i, end='')
  #new line each row
  print("")


#Exercise 9: Check Palindrome Number

#Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

num = int(input("Input number:"))
str_num = str(num)
reversed_str = str_num[::-1]
print(reversed_str)

if str_num == reversed_str:
  print("True")
else:
  print("False")

#Exercise 10: Merge two lists using the following condition

#Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result = []

for i in range(len(list1)):
  if list1[i] % 2 != 0:
    result.append(list1[i])

for i in range(len(list2)):
  if list2[i] % 2 == 0:
    result.append(list2[i])

print(result)

#Exercise 11: Get each digit from a number in the reverse order.

number = str(7536)
reversed_str = number[::-1]
print(reversed_str)

spaced_str = ' '.join(reversed_str)
print(spaced_str)