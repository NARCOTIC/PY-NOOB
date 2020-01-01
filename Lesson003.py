from array import*                                            # Import a library with all functions in it

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-003")      # Print to Screen
print()                                                       # Print an Empty Line

size = int(input("Create an array with size of : "))          # Input a value to a Integer Variable
print()                                                       # Print an Empty Line

first_array = array('i',[])                                   # Create an Array with size x and type 'i' int

for i in range(size):                                         # Loop this section in range i to n (n times)
  x = int(input("Enter value : "))                            # Input integer value
  first_array.append(x)                                       # Add it as the array's i'th element
print("Added your ", size, " values to the Array.")           # Print to Screen

print()
print("1. Search for a array element")                        # Print to Screen
print("2. Print the array")                                   # Print to Screen
print()
select = int(input("Select: "))                               # Input integer value

if select == 1:                                               # If s = 1
  print()
  item = int(input("Search for item : "))                     # Input integer value
  print()
  print("'", item, "' is at #", first_array.index(size))      # Search an item in the aray. 
                                                              

elif select == 2:                                             # If s = 2
  print()
  n = int(input("Print the first __ elements : "))            # Input integer value
  print()

  for i in range(n):                                          # Loop this section in range i to n (n times) 
    print(first_array[i])                                     # Print i'th element

print()
print("THAT'S IT FOR THIRD LESSON. TAKE A LOOK AT THE FOURTH ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
