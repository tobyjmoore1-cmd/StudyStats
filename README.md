
# StudyStats

StudyStats is a Python web application that allows users to upload CSV files containing student names and grades. It analyzes the data and displays statistics such as class average, top-performing student, and class pass rate.

## Technologies Used
- Python
- Streamlit
- Visual Studio Code
- Git and GitHub

## Features
- Upload custom CSV files
- Calculate the class average
- Find the student with the highest grade
- Calculate the class pass rate
- Adjust the minimum passing grade using a slider

## How to Run
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure Python is installed.
4. Open the terminal and install Streamlit:

   ```powershell
   python -m pip install streamlit
   ```

5. Start the application:

   ```powershell
   python -m streamlit run app.py
   ```

6. Open the local URL displayed in your terminal to use StudyStats.

## CSV File Format

Your CSV file should contain two columns: `name` and `grade`.

Example:

```csv
name,grade
Alice,95
Bob,82
Charlie,91
David,76
```

Grades should be whole numbers.
