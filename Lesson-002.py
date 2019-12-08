i = 0                                                         # Assigning a value to a Variable
x = 0                                                         # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-002")      # Print to Screen
print()                                                       # Print an Empty Line

string = input("Enter a String : ")                           # Input a String
x = int(input("Print first __ characters : "))                # Input a value to a Integer Variable
print()                                                       # Print an Empty Line

if x <= len(string):                                          # Function: len() returns the length of a String
                                                              # If the length of String is less than or equal to x
  while i < x:                                                # While Loop
    print(string[i])                                          # Print the String as an array elements
    i=i+1                                                     # Increment i by 1

else:                                                         # If the length of String is greater than x
  print("String contains only ", len(string), " items.")      # Print to Screen
  print("Cannot output ", x, " items.")                       # Print to Screen

print()
print("THAT'S IT FOR SECOND LESSON. TAKE A LOOK AT THE THIRD ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
