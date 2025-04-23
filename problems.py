# # s = input()
# # s1 = s.lower()
# # a = s1.count('a')
# # e = s1.count('e')
# # i = s1.count('i')
# # o = s1.count('o')
# # u = s1.count('u')
# # print(f"Number of vowels:{a+e+i+o+u}")

# m = int(input("Enter your marks in maths:"))
# s = int(input("Enter your marks in science:"))
# e = int(input("Enter your marks in english:"))
# total_marks = m+s+e
# average_marks = total_marks/3
# perc = (total_marks/300)*100
# grade = ""
# if perc > 90:
#     graderade = "A"
# elif perc > 80 and perc <= 90:
#     grade = "B"
# elif perc > 70 and perc <= 80:
#     grade = "C"
# else:
#     print("PASS")
# print(f"Total marks:{total_marks}\nAverage marks:{average_marks}\nGrade:{grade}")



#PALINDROME 


# s = input("Give a string:")
# reverse = s[::-1]
# if reverse == s:
#     print("palindrome")
# else:
#     print("it is not a palindrome")


# FIND THE LARGEST NUMBER IN A LIST 


# a = input("Enter three numbers seperated by space:")
# x,y,z = a.split(" ")
# num1 = int(x)
# num2 = int(y)
# num3 = int(z)

# if num1 > num2 and num1 > num3:
#     print(f"{num1}is the largest number")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2}is the largest number")
# else:
#     print(f"{num3}is the largest number")



# year = int(input("Enter a year:"))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# year = int(input())
# leap = False
# if year % 100 == 0 and year % 400 != 0:
#     leap = False
# elif year % 4 == 0:
#     leap = True
# else:
#     leap = False
# print(leap)


# temp = float(input("Enter temperature: "))
# unit = input("Enter unit of temperature (C, F, K): ").strip().upper()

# if unit == "C":
#     f = (temp * 9/5) + 32
#     k = temp + 273.15
#     print(f"Temperature in Fahrenheit: {f:.1f} F")
#     print(f"Temperature in Kelvin: {k:.1f} K")
# elif unit == "F":
#     c = (temp - 32) * 5/9
#     k = c + 273.15
#     print(f"Temperature in Celsius: {c:.1f} C")
#     print(f"Temperature in Kelvin: {k:.1f} K")
# elif unit == "K":
#     c = temp - 273.15
#     f = (c * 9/5) + 32
#     print(f"Temperature in Celsius: {c:.1f} C")
#     print(f"Temperature in Fahrenheit: {f:.1f} F")
# else:
#     print("Invalid input. Please enter a valid unit (C, F, K).")