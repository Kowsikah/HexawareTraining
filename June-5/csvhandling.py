import csv
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

#printing names of the employee
with open("employee.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])

#Employee count
count=0
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        count+=1
print("Number of employees:"+str(count))


#highestsalary
highest_sal=0
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[3])>highest_sal:
            highest_sal=int(row[3])
print("Highest Salary:"+str(highest_sal))

#lowest salary
c=0
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    lowest_sal=0
    for row in reader:
        if(c==0):
            lowest_sal=int(row[3])
            c=1
        elif int(row[3])<lowest_sal:
            lowest_sal=int(row[3])
print("Lowest Salary:"+str(lowest_sal))

#Total salary
total=0
with open("employee.csv","r") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        total+=int(row[3])
print("Total Salary:"+str(total))

#Average salary
print("Average salary:",total/count)

#Hyderabad employees
print("Employees in Hyderabad city")
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[4]=='Hyderabad':
            print(row[1])

#AI Engineering
print("Employees in AI Engineering:")
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[2]=='AI Engineering':
            print(row[1])
#employees greater 80000
print("Employee salary greater than 80000")
with open("employee.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[3])>80000:
            print(row[1])

