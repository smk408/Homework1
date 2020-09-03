# Author: Selena Kesidis smk408@psu.edu
gp = input("Enter your course 1 letter grade: ")
c1 = input("Enter your course 1 credit: ")
c1 = float(c1)

if gp == "A":
  gp1 = 4.0
elif gp == "A-":
  gp1 = 3.67
elif gp == "B+":
  gp1 = 3.33
elif gp == "B":
  gp1 = 3.0
elif gp == "B-":
  gp1 = 2.67
elif gp == "C+":
  gp1 = 2.33
elif gp == "C":
  gp1 = 2.0
elif gp == "D":
  gp1 = 1.0
else: 
  gp1 = 0.0

print(f"Grade point for course 1 is: {gp1}")
gp = input("Enter your course 2 letter grade: ")
c2 = input("Enter your course 2 credit: ")
c2 = float(c2)

if gp == "A":
  gp2 = 4.0
elif gp == "A-":
  gp2 = 3.67
elif gp == "B+":
  gp2 = 3.33
elif gp == "B":
  gp2 = 3.0
elif gp == "B-":
  gp2 = 2.67
elif gp == "C+":
  gp2 = 2.33
elif gp == "C":
  gp2 = 2.0
elif gp == "D":
  gp2 = 1.0
else: 
  gp2 = 0.0

print(f"Grade point for course 2 is: {gp2}")
gp = input("Enter your course 3 letter grade: ")
c3 = input("Enter your course 3 credit: ")
c3 = float(c3)

if gp == "A":
  gp3 = 4.0
elif gp == "A-":
  gp3 = 3.67
elif gp == "B+":
  gp3 = 3.33
elif gp == "B":
  gp3 = 3.0
elif gp == "B-":
  gp3 = 2.67
elif gp == "C+":
  gp3 = 2.33
elif gp == "C":
  gp3 = 2.0
elif gp == "D":
  gp3 = 1.0
else: 
  gp3 = 0.0

print(f"Grade point for course 3 is: {gp3}")
gpa = (gp1 * c1 + gp2 * c2 + gp3 * c3) / (c1 + c2 + c3)
print(f"Your GPA is: {gpa}")