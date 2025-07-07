assignment: Assignment_1
description: Basic Python programs to practice input/output, arithmetic operations, and string concatenation.
folder_structure:
  Assignment_1:
    - task1.py: Perform arithmetic operations (+, -, *, /)
    - task2.py: Create a personalized greeting
    - README.md: Description and instructions for the assignment

tasks:
  - name: Task 1 - Arithmetic Operations
    file: task1.py
    description: >
      Takes two numbers from the user (can be integers or floats) and performs
      addition, subtraction, multiplication, and division.
    sample_run: |
      Enter the first number: 10.5
      Enter the second number: 2
      Addition: 12.5
      Subtraction: 8.5
      Multiplication: 21.0
      Division: 5.25

  - name: Task 2 - Personalized Greeting
    file: task2.py
    description: >
      Takes the user's first and last name as input, concatenates them, and
      prints a personalized greeting message.
    sample_run: |
      Enter your first name: Alice
      Enter your last name: Johnson
      Hello, Alice Johnson! Welcome to the python program.

instructions:
  prerequisites: Ensure Python is installed and added to your system's PATH.
  how_to_run: |
    Open a terminal or command prompt and navigate to the Assignment_1 folder.
    Then run the following commands:
      python task1.py
      python task2.py
