student_scores = {
    "Pere": "98", "Douye": "89", "Morgan": "60", "Favor": "72", "Timidi": "54",
    "Sarah": "47",
}

print(student_scores["Pere"])
student_scores["Pere"] = "Scores 98"

empty_dictionary = {}
# empty_dictionary[]

# Wipe an existing_dictionary

# print(programming_dictionary)

# Edit an item in a dictionary

student_grade = {
    "Scores 91 - 100: Grade = Outstanding.",
    "Scores_81 - 90: Grade = Exceeds_Expectations.",
    "Scores 71 - 80: Grade = Acceptable.",
    "Scores 70 or lower: Grade = Fail.",
}

# Loop through a dictionary
for key in student_scores:
    print(f"name: {key}, Score: {student_scores[key]}")
for student in student_scores:

    # Get the value (student score) by using the key each time and convert it to an integer
    score = int(student_scores[student])

    # Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grade[student] = 'Outstanding'
    elif score >= 81:
        student_grade[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grade[student] = 'Acceptable'
    else:
        student_grade[student] = 'Fail'

# Print the final student_grades dictionary
print(student_grade)
print(f"name: {key}, Score: {student_scores[key]}")