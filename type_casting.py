
name = "Lance"
age = 22
gpa = 1.5
is_student = True
is_has_name = ""

#type casting
new_gpa = int(gpa)
new_age_float = float(age)
new_age_string = str(age)
name_valid = bool(is_has_name)

# outputs
print(type(name))
print(type(new_age_string))
print(type(age))

print(f"From float {gpa} into integer which is now a {new_gpa}")
print(f"From integer {age} into float {new_age_float}" )
print(f"From integer {age} into string {new_age_string}")
print(f" Does the value has inputted name? {name_valid}")