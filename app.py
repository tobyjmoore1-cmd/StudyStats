import streamlit as st
from main import load_grades, calculate_average, find_top_student
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)
st.title("StudyStats Dashboard")
st.write("Analyze your class grades!")

if uploaded_file is not None:
    students = load_grades(uploaded_file)
    average = calculate_average(students)
    top_student = find_top_student(students)
    st.success(uploaded_file.name + " uploaded successfully!")
else:
    students = load_grades("grades.csv")
    average = calculate_average(students)
    top_student = find_top_student(students)

calculate_average_button = st.button("Calculate Average")
if calculate_average_button:
    average = calculate_average(students)
    st.write(f"Class average: {average:.2f}")

find_top_student_button = st.button("Find Top Student")
if find_top_student_button:
    top_student = find_top_student(students)
    st.write(f"Top student: {top_student['name']} with grade: {top_student['grade']}")
st.metric("Class Average", f"{calculate_average(students):.2f}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Student")
    st.write(f"Name: {top_student['name']}")
    st.write(f"Grade: {top_student['grade']}")
with col2:
    st.subheader("Class Average")
    st.write(f"Average Grade: {average:.2f}")