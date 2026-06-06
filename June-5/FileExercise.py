from DatastructureExercise import lowest_salary, total_salary

with open("employees.txt") as fp:
    # Read and display entire file.
    data=fp.read()
    print(data)
    #Display file line by line.
print("Displaying line by line")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        print(line,end="")
        line=fp.readline()
count=0
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        count+=1
        line=fp.readline()
print("\nTotal number of employees: ",count)
print("Employee Names:")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        print(data[1])
        line=fp.readline()
#employees from hyderabad
print("Employees from Hyderabad:")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        city=data[4]
        if city=='Hyderabad\n':
            print(data[1])
        line=fp.readline()
#employees from bangalore
print("Employees from Bangalore:")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        city=data[4]
        if city=='Bangalore\n':
            print(data[1])
        line=fp.readline()
#employees salary whose greater than 80000
print("Employees salary whose greater than 80000")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        salary=int(data[3])
        if salary>80000:
            print(data[1])
        line=fp.readline()
#Find highest salary
highestSalary=0
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        salary=int(data[3])
        if salary>highestSalary:
            highestSalary=salary
        line=fp.readline()
print("Highest salary:",highestSalary)
with open("employees.txt") as fp:
    line=fp.readline()
    lowest_salary=int(line.split(',')[3])
    while line:
        data=line.split(',')
        salary=int(data[3])
        if salary<lowest_salary:
            lowest_salary=salary
        line=fp.readline()
print("Lowest salary:",lowest_salary)
#average salery
total_salary=0
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        salary=int(data[3])
        total_salary+=salary
        line=fp.readline()
print("Average salary:",total_salary/count)
#Total Salary
print("Total salary:",total_salary)
#Employee count in AI Engineering
employee_ai_count=0
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        if data[2]=="AI Engineering":
            employee_ai_count+=1
        line=fp.readline()
print("No of employees in AI engineering:",employee_ai_count)
employee_data_count=0
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        if data[2]=="Data Engineering":
            employee_data_count+=1
        line=fp.readline()
print("No of employees in Data engineering:",employee_data_count)
print("Employees in AI Engineering")
with open("employees.txt") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        if data[2]=="AI Engineering":
            print(data[1])
        line=fp.readline()
with open("employees.txt") as fp:
    with open("high_salary_employees.txt","w") as f:
        line = fp.readline()
        while line:
            data = line.split(',')
            salary = int(data[3])
            if salary > 80000:
                f.write(data[1])
                f.write("\n")
            line = fp.readline()
#writing names in hyderabad_employees.txt
with open("employees.txt") as fp:
    with open("hyderabad_employees.txt","w") as f:
        line = fp.readline()
        while line:
            data = line.split(',')
            city= data[4]
            if city=='Hyderabad\n':
                f.write(data[1])
                f.write("\n")
            line = fp.readline()
#Display and count unique cities
cities=set()
with open("employees.txt","r") as fp:
    line=fp.readline().rstrip()
    while line:
        data=line.split(',')
        city=data[4]
        print(city)
        cities.add(city)
        line = fp.readline().rstrip()
cities=list(cities)
print("Unique cities:")
for city in cities:
    print(city)
print("\nNumber of cities:",len(cities))
employees_details=dict()
with open("employees.txt","r") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        if employees_details.get(data[2])==None:
            employees_details[data[2]]=1
        else:
            employees_details[data[2]]=employees_details.get(data[2])+1
        line=fp.readline()
for department,count in employees_details.items():
    print(department,"=",count)
with open("employees.txt","r") as fp:
    line=fp.readline()
    while line:
        data=line.split(',')
        if int(data[3])==highestSalary:
            print(data[1])
            print(data[3])
        line=fp.readline()
with open("employee_report.txt","w") as f:
    f.write("Total Employees:"+str(count)+"\n")
    f.write("Highest Salary:"+str(highestSalary)+"\n")
    f.write("Lowest Salary:"+str(lowest_salary)+"\n")
    f.write("Average salary:"+str(total_salary/count)+"\n")
    f.write("Total Salary:"+str(total_salary)+"\n")

