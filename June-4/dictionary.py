customer={'customer_id':101,'name':'Rahul','city':'Salem'}
print(customer)

print(customer['name'])
print(customer['city'])
#safe
print(customer.get('name'))
#add new value
customer['salary']=50000
print(customer)
#update
customer['salary']=80000
print(customer)
customer.pop('salary')
print(customer)
del customer['city']