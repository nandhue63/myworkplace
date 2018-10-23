
#sets

cs_courses1 =  {'History', 'Science', 'Biology', 'Art'}
cs_courses2 =  {'History', 'Sscience', 'Bbiology', 'Art'}

print(cs_courses1)
print(cs_courses2)

print('math' in cs_courses1)

#intersection
print(cs_courses1.intersection(cs_courses2))

#union
print(cs_courses1.union(cs_courses2))

#emptyset
empty_set = set()