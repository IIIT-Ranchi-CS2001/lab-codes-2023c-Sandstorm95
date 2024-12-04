# Lists of course codes and course names
course_codes = ["CS1001", "MA1002", "PH1003"]
course_names = ["Python", "Calculus", "Physics"]

# Combine both lists
combined_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

# Print the combined list
print(combined_list)

couse_codes = ["cs", "Ma", "PH"]
corse_names = [f"{code}:{name}" for code, name in zip(couse_codes, corse_names)]