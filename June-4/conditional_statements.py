salary=35000
if salary>50000:
    print('High Income')
else:
    print('Normal Income')

salary=75000
experience=2
if salary>50000 and experience>=3:
    print('Eligible')
else:
    print('Not Eligible')

#Multiple condition
mark=85
if mark>90:
    print('Grade A')
elif mark>75:
    print('Grade B')
elif mark>60:
    print('Grade C')
else:
    print('Grade D')

is_blocked=False
#not operator
if not is_blocked:
    print('Login ALLowed')