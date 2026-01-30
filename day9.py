students = [
    {"name": "Som", "Score": 67},
    {"name": "A", "Score": 48},
    {"name": "Pap", "Score": 88},
    {"name": "Yam", "Score": 28},
    {"name": "Mint", "Score": 18},
    {"name": "Kao", "Score": 88},
    {"name": "Hu", "Score": 78},
    {"name": "Ren", "Score": 56},
    {"name": "Jean", "Score": 32},
    {"name": "Bai", "Score": 12},
    {"name": "Pao", "Score": 87},
    {"name": "Pin", "Score": 12},
    {"name": "Kim", "Score": 2},
    {"name": "Sim", "Score": 89},
    {"name": "Chin", "Score": 99},
    {"name": "Jub", "Score": 28}
]

failed_student = []

for s in students:
    if s["Score"] <= 50:
        failed_student.append(s)

passed_student = []
for s in students :
    if s["Score"] >= 50:
        passed_student.append(s)


print (f"Failed student = {failed_student}")
print (f"Passed student = {passed_student}")

total_failed = len(failed_student)
total_passed = len(passed_student)
print (f"Total Failed students is : {total_failed} students")
print (f"Total Passed students is : {total_passed} students")

def give_scholarship(data_list):
    scholarship_winner = []

    for student in data_list:
        if student["Score"] >= 85:
            student["Scholarship"] = True
            scholarship_winner.append(student)
    return scholarship_winner

winner = give_scholarship(passed_student)

print(f"List of scholarship students (Score >= 85): {winner}")
print(f"Total Scholarship students: {len(winner)} students")



