
import csv
import io

def load_grades(source):
    if isinstance(source, str):
        with open(source, "r", encoding="utf-8-sig") as f:
            text = f.read()
    else:
        text = source.getvalue().decode("utf-8-sig")

    students = []
    reader = csv.DictReader(io.StringIO(text))

    for row in reader:
        row["grade"] = int(row["grade"])
        students.append(row)

    return students


def calculate_average(students):
    total = 0
    for student in students:
        total += student["grade"]

    average = total / len(students)
    return average


def find_top_student(students):
    top_student = students[0]

    for student in students:
        if student["grade"] > top_student["grade"]:
            top_student = student

    return top_student

def calculate_pass_rate(students, passing_grade=70):
    passing_students = [student for student in students if student["grade"] >= passing_grade]
    pass_rate = len(passing_students) / len(students) * 100
    return pass_rate

if __name__ == "__main__":
    students = load_grades("grades.csv")

    average = calculate_average(students)
    top_student = find_top_student(students)

    print(f"Class average: {average:.2f}")
    print(f"Top student: {top_student['name']} with grade: {top_student['grade']}")
    pass_rate = calculate_pass_rate(students)
    print(f"Pass rate: {pass_rate:.2f}%")
