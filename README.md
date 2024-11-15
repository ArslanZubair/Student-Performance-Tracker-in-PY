
# Student Performance Tracker

This project is a Python-based system to manage and track student grades using Object-Oriented Programming concepts. It calculates averages, checks if students are passing, and provides performance feedback.

## How to Use:

- Clone the repository to your local machine or open the `.ipynb` file on Colab.
- Add student names and their scores for different subjects.
- The program will calculate the class average and individual student performance.

## Files:
- `student_performance_tracker.ipynb`: Jupyter/Colab notebook for the project.
- `student_performance_tracker.py`: Python script for the project.

## Requirements:
- Python 3.x
- If using Jupyter or Colab, simply run the cells in sequence.

## Installation:
1. Clone the repository using `git clone https://github.com/your_username/Student_Performance_Tracker.git`
2. Open the notebook in Jupyter or run the Python script directly.


Here’s a brief Markdown (`.md`) documentation file for your code:

---

# Project Description starts from here

This Python script is a **Student Performance Tracker** that allows users to add students, record their scores, and calculate both individual and class averages. The tracker evaluates each student's performance, indicating whether they are passing based on their average score and specified passing criteria.

## Code Structure

The code consists of two main classes: `Student` and `PerformanceTracker`, along with utility functions to gather student data and display results.

### Classes

#### 1. `Student`
This class represents an individual student and has two main attributes:

- **Attributes**:
  - `fullName`: Stores the full name of the student.
  - `scores`: A list of scores obtained by the student.

- **Methods**:
  - `calculate_average()`: Calculates and returns the average score of the student.
  - `is_passing(passing_score=40)`: Returns `True` if all scores are above or equal to the specified passing score, `False` otherwise.

#### 2. `PerformanceTracker`
This class tracks multiple students' performance.

- **Attributes**:
  - `students`: A dictionary that stores each student by name as a key with `Student` objects as values.

- **Methods**:
  - `add_students(student)`: Adds a `Student` object to the tracker.
  - `calculate_class_average()`: Calculates and returns the average score of all students in the tracker.
  - `display_student_performance()`: Displays each student’s name, average score, and whether they are passing.

### Utility Functions

#### 1. `get_student_data()`
Prompts the user to enter students’ names and scores for three subjects. Creates a `Student` object for each student and adds it to the `PerformanceTracker`.

#### 2. `display_results(tracker)`
Displays each student's performance details and calculates and displays the class average.

### Usage

To run the program:

1. Run the script.
2. Enter each student's name and scores for three subjects when prompted.
3. Enter `done` when all students have been added.
4. The program displays each student's performance summary and the class average.

### Example Output

```python

Enter the student's Name or type 'done' to finish: John Doe
Enter the score of subject 1: 75
Enter the score of subject 2: 60
Enter the score of subject 3: 85
...
-----------------Student Performance-----------------:
Student: John Doe | Average: 73.33 | Passing: Yes ! Congratulations
Student: Jane Smith | Average: 58.0 | Passing: No, Student Needs Improvement!
Class Average Score: 65.67
```

### Error Handling
The program also checks that all entered scores are within a valid range (0 to 100). If an invalid score is entered, the program prompts the user to enter a valid score.

