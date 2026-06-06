a=5
b=0
try:
    result=a/b
    print(result)
except:
    print("Division by zero")
finally:
     print('Program Completed')

#specific exception
try:
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Division by zero")

#another example
try:
    age=int(input("Enter your age:"))
    print(age)
except ValueError:
    print('Please Enter a numeric value')

#Multiple exceptiom
try:
    num=int('abc')
except Exception as e:
    print(e)

#Else block in exception
try:
    a=int(input("Enter your number:"))
    print(a)
except ValueError:
    print('Please Enter a numeric value')
else:
    print('Success!')
#Raise Error
salary=-1000
try:
      if salary<0:
         raise ValueError("Please Enter a numeric value")
except ValueError:
    print('Please Enter a correct numeric value')


