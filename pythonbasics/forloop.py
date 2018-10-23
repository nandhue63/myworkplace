

courses = ('History', 'Maths', 'Science', 'Biology')


#index used to get the index values of the items in the list
#enumerate used to idex and courses together
#course is variable here
#start can start the custom index number 
for index, course in enumerate(courses, start=1):
    print(index, course)