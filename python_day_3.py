# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CFXl9-CBMZutLKhyaimtJnewAV4ZiReY

#BUILD-IN FUNCTIONS IN PYTHON

#1. len( )
"""

list= [4,5,6,7,8,9,4,5,6,1,2,3]

len(list)

text = "hello world"

len(text)

fruits = ("apple", "banana", "kiwi", "cherry")

len(fruits)

student = {"name": "harsh", "age" : 10 , "grade" : "A"}

len(student)

"""#2. abs( )

returns the absolute values of a number
"""

abs(-5)

"""#3. min ( )"""

list = [5,4,6,7,8,9,1,2]

min(list)

"""#4. max ( )"""

max(list)

"""#5. sum ( )"""

list

sum(list)

"""#6. type ( )"""

type(list)

"""#7. round ()"""

number = 3.145236971

round(number)

round(number , 1)

round(number , 2)

round(number , 3)

"""#7. str ()"""

number = 123456

type(number)

str(number)

string = str(number)

type(string)

int(number)

float(number)

"""#8. dict { }"""

!python --version

dict([("name", "harsh"), ("age", 25)])

"""#9. sorted ( )  
> Add blockquote


"""

number = [7,8,9,5,4,1,2,3,6,4,7,8,9,6]

sorted(number)

number2 = reversed(number)

number2

print(number2)

letters = [ "harsh", "banana", "kiwi", "apple"]

"""# conditional statements

#1. IF statement
"""

age = 18
if age>=18:
  print("you are an adult")

age = 17
if age>=18:
  print("you are an adult")

"""#2. IF-else statement"""

#example1 - checking number is positive or not

num = 10
if num > 0:
  print("number is positive")
else:
  print("number is not positive")

num = -15
if num > 0:
  print("number is positive")
else:
  print("number is not positive")

#even odd

num = 10
num / 3

num % 3

if num % 2 == 0:
  print("the number is even")
else:
  print("the number is odd")

num = int(input("Enter the number:- "))  #ask user for the number
if num % 2 == 0:
  print("the number is even")
else:
  print("the number is odd")

a = 10
b = 20

print (a +b)

a = int(input("enter the first value :-"))
b = int (input("enter the 2nd value:-"))
print(a + b)

#password

main_password = input("set the password:-")

password = input ("enter the password:-")

if password == main_password:
  print("access granted")
else:
  print("wrong password")

"""#3. IF-ELIF-ELSE"""

#grading system

score = int(input("Enter the score:-"))

if score >= 90:
  grade = "A"
elif score >=80:
  grade ="B"
elif score >=70:
  grade ="C"
elif score >=60:
  grade ="D"
else:
  grade ="Fail"

print("your grade is :-", grade)

score = int(input("Enter the score:-"))

if score >= 90:
  grade = "A"
elif score >=80:
  grade ="B"
elif score >=70:
  grade ="C"
elif score >=60:
  grade ="D"
else:
  grade ="Fail"

print("your grade is :-", grade)

#weather statement

temperature = float(input("Enter the temp. in city"))

if temperature >=30:
  weather = "Hot"
elif temperature >=20:
  weather = "warm"
elif temperature >= 10:
  weather = "Cool"
else:
  weather = "Cold"

print("The weather is :-", weather)

temperature = float(input("Enter the temp. in city:- "))

if temperature >=30:
  weather = "Hot"
elif temperature >=20:
  weather = "warm"
elif temperature >= 10:
  weather = "Cool"
else:
  weather = "Cold"

print("The weather is :-", weather)

#number comparison - 3 number

num1 = float(input("enter 1st no. :-"))
num2 = float(input("enter 2nd no :-"))
num3 = float(input("enter 3rd no:-"))


if num1 >= num2 and num1 >= num3:
  print("number 1 is largest number")

elif num2 >= num1 and num2 >= num3:
  print("number 2 is largest number")

else:
  print("number 3 is largest number")

"""#4. Nested if statement

"""

num = 15

if num > 10:
  print("Number is grater than 10")
  if num % 2 ==0:
    print("Number is even")
  else:
    print("Number is odd")

else:
  print("Number is smaller than 10")

num = 8

if num > 10:
  print("Number is grater than 10")
  if num % 2 ==0:
    print("Number is even")
  else:
    print("Number is odd")

else:
  print("Number is smaller than 10")

"""#ATM"""

print("welcome to the ATM!")
print("1. check balance")
print("2. Deposite Money")
print("3. Withdraw Money")
print("4. Exit")


choice = int(input("Select an option (1 -4) : -"))

if choice == 1:
  print("Your current balance is $1000")

elif choice ==2:
  deposit = float (input("Enter the amount to deposit"))
  if deposit > 0:
    print ("You have successfully deposited $", deposit)
  else:
    print("Invalid deposit amount")

elif choice ==3:
  withdraw = float(input("Enter amount to withdraw"))
  if withdraw >0:
    print("You have successfully withdraw :-", withdraw)
  else:
    print("Invalid withdraw amount")

elif choice ==4:
  print("Thank you for using the ATM.. Good Day")

else:
  print("Invalid choice, Please select a valid option")

print("welcome to the ATM!")
print("1. check balance")
print("2. Deposite Money")
print("3. Withdraw Money")
print("4. Exit")

Total_Balance = 10000

choice = int(input("Select an option (1 -4) : -"))

if choice == 1:
  print("Your current balance is :-", Total_Balance)

elif choice ==2:
  deposit = float (input("Enter the amount to deposit"))
  if deposit > 0:
    print ("You have successfully deposited $", deposit)
    print ("Your Total Blance is :_", Total_Balance + deposit)
  else:
    print("Invalid deposit amount")

elif choice ==3:
  withdraw = float(input("Enter amount to withdraw"))
  if withdraw >0:
    print("You have successfully withdraw :-", withdraw)
    print("Your Total Balance is :-", Total_Balance - withdraw)
  else:
    print("Invalid withdraw amount")

elif choice ==4:
  print("Thank you for using the ATM.. Good Day")

else:
  print("Invalid choice, Please select a valid option")

"""#5. Short Hand if"""

a = 5
b = 10

print("a is grater") if a > b else print("b is grater")

"""#6. pass statement"""

age = 18
if age>=18:
  pass

"""Here are 10 questions that require the use of **nested `if-else`** statements to solve:

### Questions:

1. **Check if a Number is Positive, Negative, or Zero**:
   - Write a program that takes a number as input and checks if it is positive, negative, or zero. Additionally, if the number is positive, check if it is even or odd.

2. **Student Grade Classification Based on Marks**:
   - Write a program that takes the marks of a student as input. If the marks are above 90, print "Grade A." If they are between 75 and 90, check if they are above 85 for "Grade B+"; otherwise, "Grade B." If below 75, print "Grade C."

3. **Triangle Type Checker**:
   - Write a program that takes the lengths of three sides of a triangle and determines if it is an equilateral, isosceles, or scalene triangle. If it is a scalene triangle, check if it is a right triangle as well.

4. **Day of the Week Based on Number**:
   - Write a program that takes a number (1-7) as input and prints the corresponding day of the week. If the day is a weekday, print "Weekday," otherwise print "Weekend." Additionally, check if the day is a public holiday.

5. **Login System with Multiple Roles**:
   - Create a program that asks for a username and password. If the login is successful, check the role of the user (Admin, User, Guest) and print different welcome messages. If the login fails, print "Access Denied."

6. **Water Level Indicator**:
   - Write a program that takes the water level in a tank as input. If the level is above 75%, print "Tank is full." If it is between 50% and 75%, print "Tank is half-full." If below 50%, check if it is above 25% for "Low level," otherwise print "Tank is almost empty."

7. **Find the Largest Among Three Numbers and Check if Even or Odd**:
   - Write a program that takes three numbers as input, finds the largest number, and then checks if that number is even or odd.

8. **Electricity Bill Calculator**:
   - Write a program that calculates the electricity bill based on units consumed:
     - If units are less than 100, charge ₹5 per unit.
     - If units are between 100 and 300, charge ₹10 per unit for the first 100 units and ₹7 for the remaining.
     - If units are above 300, charge ₹15 per unit for the first 300 units and ₹10 for the remaining.

9. **Nested Grade Checker Based on Two Subjects**:
   - Write a program that takes the marks of two subjects. If both are above 60, print "Pass." If only one is above 60, print "Reappear in the failed subject." If both are below 60, print "Failed." For scores above 80 in both subjects, print "Distinction."

10. **Discount Calculation Based on Purchase Amount**:
    - Write a program that takes the total purchase amount as input and applies discounts:
      - If the amount is above ₹5000, give a 20% discount.
      - If between ₹2000 and ₹5000, give a 10% discount. If the amount is above ₹4000 in this range, add a 5% extra discount.
      - If below ₹2000, no discount is applied.

### Notes
These questions are designed to reinforce the concept of nested `if-else` statements, allowing for multi-level decision-making and handling various scenarios in a program.
"""

#3 - triange

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Checking the type of triangle
if side1 == side2 == side3:
    print("The triangle is Equilateral.")

else:
    if side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
        a, b, c = sorted([side1, side2, side3])
        if a**2 + b**2 == c**2:
            print("The Scalene triangle is also a Right Triangle.")
        else:
            print("The Scalene triangle is not a Right Triangle.")

