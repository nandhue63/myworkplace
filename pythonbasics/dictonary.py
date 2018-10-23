

student = {'name': 'Bharath', 'age': 28, 'courses': ['Math', 'Science']}


print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

print(student.get('age'))

# passing value as text for invalid key used
print(student.get('phone', 'Not found'))

# adding the new keys in to the list
student['phone']= 33333333333
print(student)

# modify the value of the key from the list
student['name']= 'Gujjula'
print(student)

# updating all the values in the list
student.update({'name': 'Nandhu', 'age': 30, 'phone': 3434343443})
print(student)

# delete the value
del student['age']
print(student)

# see all keys
print(student.keys())

# see all values only
print(student.values())

# see individual items
print(student.items())

# loop through the keys
for key, value in student.items():
    print(key, value)

