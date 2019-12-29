def interview(name, age, gpa):                                # Function Definition
  if age >= 18:                                               # If age is greater than or equal to 18
    print(name, ", You're Qualified")
  else:                                                       # Else
    print(name, ", You're not Qualified")
  gpaLetterGrade(gpa)                                         # Calling another function

def gpaLetterGrade(gpa):                                      # Function Definition
  if gpa == 4.0:                                              # If GPA is 4.0
    print("Your overall grade is A")
  elif gpa < 4.0 and gpa >= 3.0:                              # If GPA is a value between 3.0 to 4.0
    print("Your overall grade is B")
  elif gpa < 3.0 and gpa >= 2.0:                              # If GPA is a value between 2.0 to 3.0
    print("Your overall grade is C")                          
  elif gpa < 2.0 and gpa >= 1.0:                              # If GPA is a value between 1.0 to 2.0
    print("Your overall grade is D")                          
  else:                                                       # Else
    print("Your overall grade is not sufficient for the job") 

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-004")      # Print to Screen
print()                                                       # Print an Empty Line

n = input("Enter Your Name : ")                               # Input a value
a = int(input("Enter Your Age : "))                           # Input a value
g = float(input("Enter Your GPA : "))                         # Input a value

print()                                                       # Print an Empty Line
interview(n, a, g)                                            # Calling the function

print()
print("THAT'S IT FOR FOURTH LESSON. TAKE A LOOK AT THE FIFTH ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
