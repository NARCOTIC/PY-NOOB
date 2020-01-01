class Grades:                                                 # Creating a class called 'grades'
  def __init__(self, math, science, music, law):              # __init__ gets called everytime an object is created (Acts like a constructor).
    self.math = math                                          # Assign passed value to self (some object)'s 'math' variable
    self.science = science                                    # Assign passed value to self (some object)'s 'science' variable
    self.music = music                                        # Assign passed value to self (some object)'s 'music' variable
    self.law = law                                            # Assign passed value to self (some object)'s 'law' variable

  def print_grades(self):                                      # Defining the function. 'self' keyword passes the object name
    print("Math", self.math)                                  # Print self (some object)'s 'math' variable       
    print("Science", self.science)                            # Print self (some object)'s 'science' variable
    print("Music", self.music)                                # Print self (some object)'s 'music' variable
    print("Law", self.law)                                    # Print self (some object)'s 'law' variable
                                                  
                                                   

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-006")      # Print to Screen
print()                                                       # Print an Empty Line

donald_trump = Grades(25, 35, 45, 55)                         # 'Donald_Trump' is an object. __init__ gets called automatically.
                                                              # And passed values get added to this object's 'math', 'science', 'music', 'law' variables

your_math = int(input("Your Math Results : "))                # Input a value to a Integer Variable
your_science = int(input("Your Science Results : "))          # Input a value to a Integer Variable
your_music = int(input("Your Music Results : "))              # Input a value to a Integer Variable
your_law = int(input("Your Law Results : "))                  # Input a value to a Integer Variable
print()                                                       # Print an Empty Line

you = Grades(your_math, your_science, your_music, your_law)   # 'You' is an object. __init__ gets called automatically.
                                                              # And passed values get added to this object's 'math', 'science', 'music', 'law' variables
print("Donald Trump's Test Results:")
donald_trump.print_grades()                                   # Calls 'printGrades' function for 'Donald_Trump' object
print()

print("Your Test Results:")
you.print_grades()                                            # Calls 'printGrades' function for 'You' object
print()

change_grade = input("Wanna Change Your Results? [Y/N]: ")    # Input a char to a Variable

if change_grade == 'Y' or change_grade == 'y':                # If 'change_grade' equals to upper or lower case Y
  print()

  your_math = int(input("Your Math Results : "))              # Input a value to a Integer Variable
  your_science = int(input("Your Science Results : "))        # Input a value to a Integer Variable
  your_music = int(input("Your Music Results : "))            # Input a value to a Integer Variable
  your_law = int(input("Your Law Results : "))                # Input a value to a Integer Variable
  print()                                                     # Print an Empty Line

  you.math = your_math                                        # Assign value of 'Your_Math' to 'You' object's 'math' variable
  you.science = your_science                                  # Assign value of 'Your_Science' to 'You' object's 'science' variable
  you.music = your_music                                      # Assign value of 'Your_Music' to 'You' object's 'music' variable
  you.law = your_law                                          # Assign value of 'Your_Law' to 'You' object's 'law' variable

  print("Your Corrected Test Results:")
  you.print_grades()                                          # Calls 'printGrades' function for 'You' object

print()
print("THAT'S IT FOR SIXTH LESSON. TAKE A LOOK AT THE SEVENTH ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
