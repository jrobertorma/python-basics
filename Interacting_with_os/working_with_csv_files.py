import csv

# Opening CSV files
def open_csv():
    # Opening the file
    f = open("Interacting_with_os\games.csv")
    csv_file = csv.reader(f)

    # Iterating over the file
    for row in csv_file:
        title,hours_played,ttb,value,d_price,price_hours,r_date,metascore,mb_size,c_support,genres = row
        print("Title: {}, Hours played: {}".format(title, hours_played))

    f.close()


# Generating CSV files
def save_data_on_csv(data_list, file_name):
    with open(file_name, "w") as new_csv:
        writer = csv.writer(new_csv)
        writer.writerows(data_list)

data_to_store = [
    ["Name", "Lastname"],
    ["John", "Lennon"],
    ["Paul", "McCartney"],
    ["Ringo", "Starr"],
    ["George", "Harrisonn"]
]
# save_data_on_csv(data_to_store,"new_csv.csv")


# Reading CSV file as a dictionary
def read_csv_as_dictionary():
    with open("Interacting_with_os\games.csv") as games:
        reader = csv.DictReader(games)
        for row in reader:
            print("Title: {}, Hours played: {}".format(row["Title"], row["Hours played"]))


# Writing CSV file from a list of dictionaries
def write_csv_from_dict():
    users = [
        {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
        {"name": "Lio Nelson", "username": "lion", "department": "UX research"},
        {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
    ]

    keys = ["name", "username", "department"]

    with open("emps.csv", "w") as emps_csv:
        # Need to set the column names with fieldnames=keys
        writer = csv.DictWriter(emps_csv, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)

# write_csv_from_dict()


# We're working with a list of flowers and some information about each one. 
# The create_file function writes this information to a CSV file. 
# The contents_of_file function reads this file into records and returns 
# the information in a nicely formatted block.
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as csv_file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(csv_file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


# Final project, a script that reads a file, parses it and builds a report using the provided file's data

#!/usr/bin/env python3
import csv


def read_employees(csv_file_location):
  employee_list = []
  with open(csv_file_location) as csv_file:
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    reader = csv.DictReader(csv_file,dialect = 'empDialect')
    for data in reader:
      employee_list.append(data)
  return employee_list


def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)

  return department_data


def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()


employee_list = read_employees("/home/student-03-e0ad12c300c2/data/employees.csv")
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student-03-e0ad12c300c2/test_report.txt')

