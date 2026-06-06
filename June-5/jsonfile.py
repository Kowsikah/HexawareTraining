import json

employees = [
    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },
    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },
    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },
    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },
    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }
]


with open("employees.json", "w") as f:
    json.dump(employees, f, indent=4)

print("JSON file created successfully\n")


with open("employees.json", "r") as f:
    loaded_employees = json.load(f)

# Loop using distinct variable names
print("Employee Names:")
for emp in loaded_employees:
    print(f"- {emp['name']}")

# This will now correctly output 5 (the number of items in the list)
print(f"\nTotal Employees: {len(loaded_employees)}")

# Highest salary logic
high_salary = 0
for emp in loaded_employees:
    if emp["salary"] > high_salary:
        high_salary = emp["salary"]

print(f"Highest Salary: {high_salary}")

#average salary
total_salary = 0
for emp in loaded_employees:
    total_salary += emp["salary"]
print("Average salary:",total_salary/len(loaded_employees))

#employees in data engineering
for emp in loaded_employees:
    if emp['department'] == "Data Engineering":
        print(f"{emp['name']}")

#employees earning more than 80000
for emp in loaded_employees:
    if emp['salary'] > 80000:
        print(f"{emp['name']}")

#update
loaded_employees[1]["salary"]=85000

loaded_employees.append(  {
        "employee_id": 106,
        "name": "Ali",
        "department": "AI Engineering",
        "salary": 80000,
        "city": "Delhi"
    }
)
with open("employees.json", "w") as f:
    json.dump(loaded_employees, f, indent=4)

updated_employees = list()
for emp in loaded_employees:
    if emp['employee_id'] !=105:
        updated_employees.append(emp)

with open("employees.json", "w") as f:
    json.dump(updated_employees, f, indent=4)
