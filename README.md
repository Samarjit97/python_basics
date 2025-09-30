📘 Python Basics

This repository contains a collection of beginner-friendly Python projects that demonstrate fundamental concepts in computer science, software development, and data analysis.

The goal of these projects is to practice problem-solving, algorithms, data handling, and program structure in Python.

Projects Overview

🔹 Algorithms

Binary Search (search_algorithms.py)
Efficiently finds an element in a sorted list using divide-and-conquer.
Good for showing understanding of algorithm efficiency (O(log n)).

Bubble Sort (sorting_algorithms.py)
Classic sorting algorithm that repeatedly swaps adjacent elements.
Includes an optimization to stop early if the list is already sorted.

🔹 Apps

Calculator (calculator.py)
A simple calculator supporting addition, subtraction, multiplication, and division.
Demonstrates function design and input validation.

To-Do List (todo_list.py)
Console-based to-do list app where tasks persist in a local file (tasks.json).
Shows file handling and user interaction.

🔹 Data Analysis

COVID Analysis (covid_analysis.py)
Uses pandas and matplotlib to analyze COVID-19 case data.

Summary statistics printed with pandas.describe().

Line plot of cases and deaths.

Bar chart and pie chart for better visualization.
Demonstrates Python data analysis and visualization libraries.

🔹 Database

Student Database (student_db.py)
Implements a basic SQLite3 database for storing student records (name + grade).

Creates a table if it doesn’t exist.

Inserts sample records.

Reads and displays students in a neat table format.

Supports CRUD operations (Create, Read, Update, Delete).

students.db
A local SQLite database file created on first run.

**Key Learning Outcomes**

Writing clean, commented Python code.

Understanding algorithms and complexity.

File handling and persistence.

Data visualization with matplotlib and pandas.

Working with relational databases using SQLite.

Organizing a project into modules and folders.

**Notes**

students.db is included so the database example works out-of-the-box.

todo_list.py creates a tasks.json file in the apps/ folder to save tasks.

All scripts are self-contained and can be run individually.

