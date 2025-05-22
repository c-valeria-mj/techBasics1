from sys import argv
import csv
import random

# Step 1
def read_csv(filename):
    # load csv to variables in your program
    # handle file exceptions here
    pass

# Step 2
def populate_scores():
    pass

# Step 3
def calculate_all():
    # loop through all the students and calculate grades
    pass

def calculate_total(scores):
    total = 0
    return total

def calculate_average(scores):
    average =  0
    return average

# After the update let's save the data as a new csv file

def write_csv(filename):
    pass

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    pass

if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "[your_name]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`