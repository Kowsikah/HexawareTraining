cities=["Hyderabad","Mumbai","Delhi"]
print(cities[0])
print(cities[1])
print(cities[2])
#Negative Indexing
print(cities[-1])
#Updating
cities[1]='Bangalore'
print(cities)
#appending
cities.append("Chennai")
print(cities)
#inserting single value
cities.insert(1,"Pune")
print(cities)
#inserting multiple values
cities.extend(["Kochin","Pondi"])
print(cities)
#removing the element
cities.remove("Pondi")
print(cities)
#remove last element
cities.pop()
print(cities)
#remove index element
cities.pop(1)
print(cities)
#delete
del cities[0]
print(cities)
#length of the list
print(len(cities))
#Membership -in
print("Mumbai" in cities)
#sort
cities.sort()
print(cities)

cities.clear()
