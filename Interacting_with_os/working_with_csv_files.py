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
        writer = csv.DictWriter(emps_csv, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)

write_csv_from_dict()
