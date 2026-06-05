cities=("Hyderabad","Mumbai","Delhi")
print(cities[0])
print(cities[1])
print(cities[2])
#Negative Indexing
print(cities[-1])
print(cities[1:4])
#length of the list
print(len(cities))
#Membership -in
print("Mumbai" in cities)
#sort

print(cities)

employee=(101,'Shyam',20000)
employee_id,employee_name,employee_salary=employee
print(employee_id)
print(employee_name)
print(employee_salary)

#multiple values
def get_employee():
    return employee_id,employee_name,employee_salary
result=get_employee()
print(result)

#Each record in python is considered as tuple
record=(101,'Rahul','Hyderabad',50000)
print(record)
