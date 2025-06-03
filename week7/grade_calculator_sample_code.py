import csv, random
from sys import argv

# Debugging flag
DEBUG = False

# General Helper functions for converting data into desired type
def get_scores(row:dict):
    # get a list of scores from a dictionary representation of a row
    scores = []
    # loop through the weeks
    for i in range(1, 13 + 1):
        if i == 6:
            continue
        content = row["week" + str(i)]
        score = get_score(content)
        scores.append(score)
    return scores

def get_score(content:str):
    # get an int score from a string cell
    # deal with special cases
    if content == "-" or content == "":
        content = "0"
    return int(content)

# Step 1
def read_csv(file:str):
    # init empty rows and col_names
    rows = []
    col_names = []
    try:
        with open(file) as f:
            reader = csv.DictReader(f)
            col_names = reader.fieldnames
            for row in reader:
                rows.append(row)
        print(f"Step 1 : Loaded data from {filename}")
    except FileNotFoundError:
        print("The file example.txt was not found")
    # Using global variables is possible but not the best idea, so let's passing them around
    return col_names, rows

# Step 2
def populate_scores(col_names, rows):
    # populate scores between week 7 - 13
    for row in rows:
        # remember each row is a dictionary now
        # print(row)
        if row["Name"] == "":  # skip empty rows
            continue
        for i  in range(7, 13+1):
            # I will first make sure the loop is correct before writing anything into the loop
            # print(i)
            value = random.randint(0,3)
            # or just assign 3 to all the weeks
            # value = 3
            row[f"week{i}"] = str(value) # assign value to the dict

    # fill up the col_names up to 13 based on the latest week
    last_name = col_names.pop()
    last_week = int(last_name[-1])
    for i in range(last_week, 13 + 1):
        col_names.append(f"week{i}")

    return col_names, rows

# Step 3
def calculate_all(col_names, rows):

    # Loop through all the students and calculate grades
    for row in rows:
        if row["Name"] == "":  # skip empty rows
            continue
        # It's easier to calculate total and average if I have a list of integers
        # so that would be my goal here to get a list of integers from a dictionary(row)
        scores = get_scores(row)
        # print(scores)
        row["total"] =  f"{calculate_total(scores)}"
        row["average"] = f"{calculate_average(scores):.2f}" # better formatting for float

    col_names.append("total")
    col_names.append("average")

    return col_names, data

def calculate_total(scores:list):
    # sort the best 10 results from scores and return the total
    scores.sort()
    best_10 = scores[:10]
    return sum(best_10)

def calculate_average(scores:list):
    # This function only handles simple data processing, it takes a list of scores and output the average
    return sum(scores)/len(scores)

def write_csv(file, col_names, rows):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_names)  # specify fieldnames as a parameter
        writer.writeheader()  # First writeheader() then writerow()
        writer.writerows(rows)
    print("New file written:", file)

# Bonus: okay I realised this can be a bit challenging, but here is a reference solution
def print_analysis(rows):
    # I want to reuse calculate_average for any average calculation, so my goal is to get a list of corresponding scores for each situation
    stream_A = []
    stream_B = []

    # I want weeks to be a dictionary, with keys: week1,week2, week3..., within each week it's a list of scores
    weeks = {}

    for row in rows:
        if row["Name"] == "":
            continue
        # reuse get_scores
        scores = get_scores(row)

        if row["Stream"] == "A":
            stream_A.extend(scores) # Just make everything into a big list here
        elif row["Stream"] == "B":
            stream_B.extend(scores)
        for i in range(1, 13+1):
            if i == 6: # skip week 6 again
                continue
            score = get_score(row[f"week{i}"])

            # if the key doesn't exist in the dict yet, create one
            if f"week{i}" not in weeks:
                weeks[f"week{i}"] = []

            weeks[f"week{i}"].append(score)

    print(f"Average Score for Stream A is: {calculate_average(stream_A):.2f}")
    print(f"Average Score for Stream B is: {calculate_average(stream_B):.2f}")


if __name__ == "__main__":
    script, filename = argv

    fieldnames, data = read_csv(filename)

    if DEBUG:
        print(data)
        print(fieldnames)

    fieldnames, data = populate_scores(fieldnames, data)

    fieldnames, data = calculate_all(fieldnames, data)

    # After the update let's save the data as a new csv file

    user_name = "[your_name]"
    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"

    write_csv(newname, fieldnames, data)
    print_analysis(data)

# Run the file with `python grade_calculator.py sheet.csv`