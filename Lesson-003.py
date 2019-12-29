from array import*                                            # Import a library with all functions in it

i = 0                                                         # Assigning a value to a Variable
n = 0                                                         # Assigning a value to a Variable
x = 0                                                         # Assigning a value to a Variable
s = 0                                                         # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-003")      # Print to Screen
print()                                                       # Print an Empty Line

n = int(input("Create an array with size of : "))             # Input a value to a Integer Variable
print()                                                       # Print an Empty Line

first = array('i',[])                                         # Create an Array with size x and type 'i' int

for i in range(n):                                            # Loop this section in range i to n (n times)
  x = int(input("Enter value : "))                            # Input integer value
  first.append(x)                                             # Add it as the array's i'th element
print("Added your ", n, " values to the Array.")              # Print to Screen

print()
print("1. Search for a array element")                        # Print to Screen
print("2. Print the array")                                   # Print to Screen
print()
s = int(input("Select: "))                                    # Input integer value

if s == 1:                                                    # If s = 1
  print()
  n = int(input("Search for item : "))                        # Input integer value
  print()
  print("Item '", n, "' is the element #", first.index(n)+1)  # Search an item in the aray. 
                                                              # +1 is there because array starts from 0

elif s == 2:                                                  # If s = 2
  print()
  n = int(input("Print the first __ elements : "))            # Input integer value
  print()

  for i in range(n):                                          # Loop this section in range i to n (n times) 
    print(first[i])                                           # Print i'th element

print()
print("THAT'S IT FOR THIRD LESSON. TAKE A LOOK AT THE FOURTH ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
