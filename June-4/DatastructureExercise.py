salaries = [45000, 55000, 65000, 75000, 85000]
#display salaries
print(salaries)
#highest
print("Maximum salary:",max(salaries))
#lowest
print("Minimum salary:",min(salaries))
#total
print("total:",sum(salaries))
#average
print("Average:",sum(salaries)/len(salaries))
#Add 95000,10500
salaries.append(95000)
print(salaries)
#remove 5500
salaries.remove(55000)
print(salaries)
#sort salaries ascending
salaries.sort()
print("Salaries in ascending:",salaries)
#sort salaries descending
salaries.sort(reverse=True)
print("Salaries in descending:",salaries)
#second highest salary
print("Second highest salary:",salaries[1])
#Display salaries greater than ₹70,000.
print(list(filter(lambda x:x>70000,salaries)))
employee = (101,"Rahul Sharma","Data Engineering",75000)
#Display all employee
print(employee)
#display employee name
print(employee[1])
#display department
print(employee[2])
employee_id,employee_name,employee_department,employee_salary = employee
print("Employee ID:",employee_id)
print("Employee Name:",employee_name)
print("Employee Department:",employee_department)
print("Employee Salary:",employee_salary)
#length of the tuple
print("Length:",len(employee))
#first element
print(employee[0])
#last element
print(employee[-1])
batch_a = {"Rahul","Priya","Amit","Sneha","Farhan"}
batch_b = {"Priya","Sneha","Neha","Arjun","Farhan"}
#common students
print("Common Students:",batch_a.intersection(batch_b))
#students only in batch A
print(batch_a.difference(batch_b))
#students only in batch b
print(batch_b.difference(batch_a))
#Find all unique students
print(batch_a.union(batch_b))
#students present in one batch
print(batch_a.symmetric_difference(batch_b))
employee_info = {
"employee_id": 101,
"name": "Rahul Sharma",
"department": "Data Engineering",
"salary": 75000,
"city": "Hyderabad"
}
print("Employee name:",employee_info["name"])
print("Employee department:",employee_info["department"],"Employee city:",employee_info["city"])
employee_info["experience"] = 5
employee_info["salary"] =85000
print(employee_info)
employee_info.pop('city')
print(employee_info)
#display all key
print(employee_info.keys())
#display all values
print(employee_info.values())
#display all key-value pairs
print(employee_info)
employees = [
{
"id": 101,
"name": "Rahul",
"department": "IT",
"salary": 50000
},
{
"id": 102,
"name": "Priya",
"department": "HR",
"salary": 70000
},
{
"id": 103,
"name": "Amit",
"department": "IT",
"salary": 60000
},
{
"id": 104,
"name": "Sneha",
"department": "Finance",
"salary": 80000
},
{
"id": 105,
"name": "Farhan",
"department": "IT",
"salary": 90000
}
]
print("employee names")
for  i in range (len(employees)):
    print(employees[i]['name'])
print("employee names")
for  i in range (len(employees)):
    if employees[i]['department'] == 'IT':
        print(employees[i]['name'])
lowest_salary = employees[0]['salary']
highest_salary = employees[0]['salary']
for  i in range (len(employees)):
    if employees[i]['salary'] < lowest_salary:
        lowest_salary = employees[i]['salary']
    elif employees[i]['salary'] > highest_salary:
        highest_salary = employees[i]['salary']
#lowest salary
print(lowest_salary)
#highest salary
print(highest_salary)
total_salary =0
for i in range (len(employees)):
    total_salary += employees[i]['salary']
#employees earning more than 70000
for i in range (len(employees)):
    if employees[i]['salary'] > 70000:
        print(employees[i])
#count employees in IT
count=0
for  i in range (len(employees)):
    if employees[i]['department'] == 'IT':
        count+=1
print("Employee count:",count)
# Sorting the employees by salary in descending order
sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)
print("Employee names sorted by salary descending:")
for emp in sorted_employees:
    print(emp['name'])
# Extract all unique salaries and sort them in descending order
unique_salaries = sorted(list(set(emp['salary'] for emp in employees)), reverse=True)

# Ensure there are at least two distinct salary records
if len(unique_salaries) >= 2:
    second_highest_salary = unique_salaries[1]
    second_highest_emp = [emp for emp in employees if emp['salary'] == second_highest_salary]
    for emp in second_highest_emp:
        print(f"Name: {emp['name']}, Salary: {emp['salary']}")
else:
    print("Not enough unique salary data available.")

#Department without duplicates
unique_departments = set(emp['department'] for emp in employees)
print("All departments (without duplicates):")
for dept in unique_departments:
    print(dept)
