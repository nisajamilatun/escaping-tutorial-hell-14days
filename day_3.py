# # Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)

# First $10,000	  0
# Next $10,000	  10
# The remaining	  20

income = 45000
tax_payable = 0

print("Given income", income)

if income <= 10000:
  #no tax
  tax_payable = 0
elif income <= 20000:
  #no tax in first 10000
  x = income - 10000
  #tax 10%
  tax_payable = x * 10/100
else:
  #first 10000
  tax_payable = 0
  #next 10000 10% tax
  tax_payable = 10000 * 10/100
  #remaining 20% tax
  tax_payable += (income-20000) * 20/100

print("Total tax to pay is", tax_payable)

# Exercise 13: Print multiplication table from 1 to 10
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
# Write a code to generates a complete multiplication table for numbers 1 through 10.

#rows
for i in range(1,11):
  #column
  for j in range(1,11):
    print(i * j, end=' ') #fungsi end= ' ', untuk memberi spasi antar angka
  print( )   #untuk jadi rows 



# Exercise 14: Print a downward half-pyramid pattern of stars
# kalo mau downward harus pake step -1

rows = 5
#row
for i in range(rows + 1, 0, -1): #start, stop, step
  #column
  for j in range(0, i-1): #start, stop
    print("*", end=' ')
  print()

# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
  if exp >=0:
    return base ** exp

base = int(input("Base ="))
exp = int(input("Exponent ="))

print(base,"raises to the power of", exp, " is :", exponent(base, exp))

#ngetes doang email baru