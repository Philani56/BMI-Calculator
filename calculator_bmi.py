import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('bmi_data.db')
c = conn.cursor()

# Create table if not exists
# Execute SQL command to create a table to store BMI data if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS bmi_data (
                id INTEGER PRIMARY KEY,
                name TEXT,
                weight REAL,
                height REAL,
                bmi REAL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )''')
conn.commit()

# Function to save BMI data to the database
def save_bmi_data(name, weight, height, bmi):
    # Execute SQL command to insert BMI data into the database
    c.execute('''INSERT INTO bmi_data (name, weight, height, bmi) VALUES (?, ?, ?, ?)''', (name, weight, height, bmi))
    conn.commit()

# Function to retrieve BMI data for a specific user
def get_user_bmi_data(name):
    # Execute SQL command to select BMI data for a specific user from the database
    c.execute('''SELECT weight, height, bmi, timestamp FROM bmi_data WHERE name = ? ORDER BY timestamp DESC''', (name,))
    return c.fetchall()

# Function to calculate BMI
def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)
    return weight / (height ** 2)

# Function to interpret BMI value
def interpret_bmi(bmi):
    # Interpret BMI value based on categories: Underweight, Normal weight, Overweight, Obese
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to calculate and display BMI
def calculate_and_display_bmi(name, weight, height):
    try:
        weight = float(weight)
        height = float(height)
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f} ({interpret_bmi(bmi)})")

        # Save data to database
        save_bmi_data(name, weight, height, bmi)

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

# Function to display historical BMI data for a user
def display_user_bmi_data(name):
    user_data = get_user_bmi_data(name)
    if user_data:
        print("Historical BMI Data:")
        for data in user_data:
            print(f"Date: {data[3]}, Weight: {data[0]}, Height: {data[1]}, BMI: {data[2]}")
    else:
        print("No data found for this user")

# Command-line interface
def main():
    while True:
        print("\nBMI Calculator")
        print("1. Calculate BMI")
        print("2. View Historical BMI Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            weight = input("Enter your weight (kg): ")
            height = input("Enter your height (m): ")
            calculate_and_display_bmi(name, weight, height)

        elif choice == "2":
            name = input("Enter your name: ")
            display_user_bmi_data(name)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

# Code Attribution
    
# Author.   Python
# Title.    sqlite3 — DB-API 2.0 interface for SQLite databases¶
# Url.      https://docs.python.org/3/library/sqlite3.html 
# Year.     2024
    
# Author.   solaearn
# Title.    BMI CALCULATOR (PYTHON BEGINNER PROJECT) 
# Url.      https://www.sololearn.com/en/Discuss/2686226/bmi-calculator-python-beginner-project 
# Year.     5th Feb. 2021
    
