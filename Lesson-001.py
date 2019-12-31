i = 0                                                         # Assigning a value to a Variable
x = 0                                                         # Assigning a value to a Variable
y = 0                                                         # Assigning a value to a Variable
z = 0                                                         # Assigning a value to a Variable
n = 0                                                         # Assigning a value to a Variable
c = 0                                                         # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-001")      # Print to Screen
print()                                                       # Print an Empty Line

x = int(input("Enter x Value : "))                            # Input a value to a Integer Variable
y = int(input("Enter y Value : "))                            # Input a value to a Integer Variable
c = int(input("Enter Common Factor : "))                            # Input a value to a Integer Variable
n = input("Enter Your Name : ")                               # Input a String

zA = x + y                                                    # Addition
zS = x - y                                                    # Substraction
zM = x * y                                                    # Multiplication
zD = x / y                                                    # Division

print()
print("Hello ", n)                                            # Printing a String with other Text
print()
print("Sum of x and y is :", zA)                              # Sum
print("Difference of x and y is :", zS)                       # Difference
print("Product of x and y is :", zM)                          # Product
print("Quotient of x and y is :", zD)                         # Quotient
print()

if (zA % 2) == 0:                                             # If the Remainder of zA is 0 after deviding by 2
  print("Sum of x and y is Even")                             # In other words: if zA is Even

else:                                                         # If the Remainder of zA is 1 after deviding by 2
  print("Sum of x and y is Odd")                              # In other words: if zA is Odd
    
if zA < 0:                                                    # If sum of x and y is less than 0
  print("Sum of x and y is a Negative Number")
    
elif zA > 0:                                                  # Else If sum of x and y is greater than 0
  print("Sum of x and y is a Positive Number")
    
else:                                                         # Else sum of x and y is = 0
  print("Sum of x and y is 0")

if x % c == 0 and y % c == 0:                                 # Using 'and' Logical Operation with if Condition
  print("x and y both have common factor:", c)

elif x % c == 0 or y % c == 0:                                # Using 'and' Logical Operation with if Condition
  print("x or y has common factor:", c)

else:                                                         # Else
  print("x or y does not have common factor:", c)

print()
print("THAT'S IT FOR FIRST LESSON. TAKE A LOOK AT THE SECOND ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
