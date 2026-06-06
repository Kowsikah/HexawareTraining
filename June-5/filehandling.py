fp=open('employee.txt','r')
data=fp.read()
print(data)
fp.close() #if the object is not closed it will be in memory

#reading one line
fp=open('employee.txt','r')
print(fp.readline())

#multiple lines
fp=open('employee.txt','r')
print(fp.readlines())

#with block -no need to close compiler will handle it
with open('employee.txt','r') as f:
    data=f.readlines()
    print(data)

#
with open('employee1.txt','w') as f:
    f.write('Rahul\n')
    f.write('Priya\n')

#Appended
with open('employee1.txt','a') as f:
    f.write('Ram')