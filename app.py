import streamlit as st
from main import calculate_pass_rate, load_grades, calculate_average, find_top_student
st.title("StudyStats Dashboard")
st.write("Analyze your class grades!")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)


if uploaded_file is not None:
    students = load_grades(uploaded_file)
    st.success(uploaded_file.name + " uploaded successfully!")
else:
    students = load_grades("grades.csv")

average = calculate_average(students)
top_student = find_top_student(students)

pass_rate_slider = st.slider("Passing Grade", min_value=0, max_value=100, value=70)
pass_rate = calculate_pass_rate(students, passing_grade=pass_rate_slider)
st.metric("Pass Rate", f"{pass_rate:.2f}%")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Student")
    st.write(f"Name: {top_student['name']}")
    st.write(f"Grade: {top_student['grade']}")
with col2:
    st.subheader("Class Average")
    st.write(f"Average Grade: {average:.2f}")