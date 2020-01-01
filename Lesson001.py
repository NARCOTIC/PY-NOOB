i = 0                                                         # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-001")      # Print to Screen
print()                                                       # Print an Empty Line

x = int(input("Enter x Value : "))                            # Input a value to a Integer Variable
y = int(input("Enter y Value : "))                            # Input a value to a Integer Variable
common_factor = int(input("Enter Common Factor : "))          # Input a value to a Integer Variable
name = input("Enter Your Name : ")                            # Input a String

sum_xy = x + y                                                # Addition
dif_xy = x - y                                                # Substraction
product_xy = x * y                                            # Multiplication
division_xy = x / y                                           # Division

print()
print("Hello ", name)                                         # Printing a String with other Text
print()
print("Sum of x and y is :", sum_xy)                          # Sum
print("Difference of x and y is :", dif_xy)                   # Difference
print("Product of x and y is :", product_xy)                  # Product
print("Quotient of x and y is :", division_xy)                # Quotient
print()

if (sum_xy % 2) == 0:                                         # If the Remainder of sum_xy is 0 after deviding by 2
  print("Sum of x and y is Even")                             # In other words: if sum_xy is Even

else:                                                         # If the Remainder of sum_xy is 1 after deviding by 2
  print("Sum of x and y is Odd")                              # In other words: if sum_xy is Odd
    
if sum_xy < 0:                                                # If sum of x and y is less than 0
  print("Sum of x and y is a Negative Number")
    
elif sum_xy > 0:                                              # Else If sum of x and y is greater than 0
  print("Sum of x and y is a Positive Number")
    
else:                                                         # Else sum of x and y is = 0
  print("Sum of x and y is 0")

if x % common_factor == 0 and y % common_factor == 0:         # Using 'and' Logical Operation with if Condition
  print("x and y both have common factor:", common_factor)

elif x % common_factor == 0 or y % common_factor == 0:        # Using 'and' Logical Operation with if Condition
  print("x or y has common factor:", common_factor)

else:                                                         # Else
  print("x or y does not have common factor:", common_factor)

print()
print("THAT'S IT FOR FIRST LESSON. TAKE A LOOK AT THE SECOND ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
