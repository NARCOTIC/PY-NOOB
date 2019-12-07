i = 0                                           # Assigning a value to a Variable
x = 0                                           # Assigning a value to a Variable
y = 0                                           # Assigning a value to a Variable
z = 0                                           # Assigning a value to a Variable
n = 0                                           # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC")     # Print to Screen
print()                                         # Print an Empty Line

x = input("Enter x Value : ")                   # Input a value to a Variable
y = input("Enter y Value : ")                   # Input a value to a Variable

zA = int(x) + int(y)                            # Addition
zS = int(x) - int(y)                            # Substraction
zM = int(x) * int(y)                            # Multiplication
zD = int(x) / int(y)                            # Division

print()
print("Sum of x and y is :", zA)                # Sum
print("Difference of x and y is :", zS)         # Difference
print("Product of x and y is :", zM)            # Product
print("Quotient of x and y is :", zD)           # Quotient
print()

if (zA % 2) == 0:                               # If the Remainder of zA is 0 after deviding by 2
  print("Sum of x and y is Even")               # In other words: if zA is Even
    
  if zA < 0:                                    # If sum of x and y is less than 0
    print("Sum of x and y is a Negative Number")
    
  elif zA > 0:                                  # Else If sum of x and y is greater than 0
    print("Sum of x and y is a Positive Number")
    
  else:                                         # Else sum of x and y is = 0
    print("Sum of x and y is 0")

else:                                           # If the Remainder of zA is 1 after deviding by 2
  print("Sum of x and y is Odd")                # In other words: if zA is Odd

  if zA < 0:                                    # If sum of x and y is less than 0
    print("Sum of x and y is a Negative Number")
    
  elif zA > 0:                                  # Else If sum of x and y is greater than 0
    print("Sum of x and y is a Positive Number")
    
  else:                                         # Else sum of x and y is = 0
    print("Sum of x and y is 0")

print()
print("THAT'S IT FOR FIRST LESSON. TAKE A LOOK AT THE SECOND ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")