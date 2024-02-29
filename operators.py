print ("what  are your best subjects(seperated by comma)")
best_subjects = input()
subjects = best_subjects.split(" ,")

print ("what are your favourite courses")
f_course = input()
courses = f_course.split (" ,")




# for subject in subjects:
#     if subject in courses:frggvfbhnjmknmc   cv    
#         print(f" your {subject} is found in my  courses.")
#     else:
#         print(f" your {subject}  is not found in my courses.")



similar_items = []
different_items = []

for subject in subjects:
    if subject in courses:
        if subject not in similar_items:
            similar_items.append(subject)
    else:
        if subject not in different_items:
            different_items.append(subject)

for course in courses:
    if course not in subjects and  course not in different_items:
        different_items.append(course)


print(similar_items)
print(different_items)
#         for subject in found_subjects:
#           print(f"Your {subject} is found in my courses.")


# for subject in not_found_subjects:
#     print(f"Your {subject} is not found in my courses.")





a = 33
b = 200
if b > a:
  print("b is greater than a")

