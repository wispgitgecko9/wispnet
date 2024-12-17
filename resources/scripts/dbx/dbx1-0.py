#####################################################
#WISPNET dbx Model 1-Origin    | Created 12.17.2024 #
#####################################################


import os
from datetime import datetime

def intro():
    print("Welcome to WISPNET experimental network. The following series of questions are from a test script which creates a file")
    print("based on the input you provide here. This script is used solely for educational and experimental purposes for the time being.")

def get_input(prompt):
    return input(f"{prompt}: ").strip()

def fileinfo():
    return get_input("Please input your full name in this format - [LAST_FIRST]")

def nameinfo():
    firstname = get_input("First name")
    middlename = get_input("Middle name")
    lastname = get_input("Last name")
    return firstname, middlename, lastname

def ageinfo():
    return get_input("Age")

def dobinfo(firstname, lastname):
    while True:
        dob = get_input(f"What is {firstname} {lastname}'s Date of Birth? (Birthday) Please provide in mmm/dd/yy format")
        try:
            rdob = datetime.strptime(dob, "%b/%d/%y").strftime("%m/%d/%y")
            ndob = datetime.strptime(dob, "%b/%d/%y").strftime("%B %d, %Y")
            return rdob, ndob
        except ValueError:
            print("Invalid date format. Please try again.")

def collect_multiple_entries(entity, name):
    entries = []
    count = int(get_input(f"How many {entity} does {name} have?"))
    for i in range(1, count + 1):
        entries.append(get_input(f"{entity} No. {i}"))
    return entries

def profcheck(data):
    print("Ok, that's it. Does this information look correct? (y/n)")
    for key, value in data.items():
        print(f"{key}: {value}")

    if get_input("").lower() != 'y':
        print("Please restart this program to re-enter the information.")
        exit(1)

def filecreate(filename, data):
    os.makedirs("prof_test_20", exist_ok=True)
    filepath = os.path.join("prof_test_20", f"{filename}.txt")

    with open(filepath, "w") as file:
        for key, value in data.items():
            if isinstance(value, list):
                file.write(f"{key}:\n")
                for idx, entry in enumerate(value, 1):
                    file.write(f"  {idx}: {entry}\n")
            else:
                file.write(f"{key}: {value}\n")

    print(f"Registry complete. File created at {filepath}.")

def main():
    
    print()
    
    intro()
    
    print()
    
    filename = fileinfo()
    firstname, middlename, lastname = nameinfo()
    age = ageinfo()
    rdob, ndob = dobinfo(firstname, lastname)

    print()

    phone_numbers = []
    if get_input(f"Are there any phone numbers associated with {firstname} {lastname}? (y/n)").lower() == 'y':
        phone_numbers = collect_multiple_entries("phone numbers", firstname)

    print()
   
    emails = []
    if get_input(f"Are there any emails associated with {firstname} {lastname}? (y/n)").lower() == 'y':
        emails = collect_multiple_entries("emails", firstname)

    print()
  
    cars_and_plates = []
    if get_input(f"Are there any license plates associated with {firstname} {lastname}? (y/n)").lower() == 'y':
        count = int(get_input(f"How many plates are associated with {firstname} {lastname}?"))
        for i in range(1, count + 1):
            car_make = get_input(f"Make (e.g., Honda) for Car {i}")
            car_model = get_input(f"Model (e.g., Accord) for Car {i}")
            plate = get_input(f"Plate No. {i}")
            cars_and_plates.append(f"{car_make} {car_model}, Plate: {plate}")

    print()
   
    data = {
        "NAME": f"{firstname} {middlename} {lastname}",
        "Age": age,
        "Date of Birth": f"{ndob} (Abbreviated: {rdob})",
        "Phone Numbers": phone_numbers,
        "Emails": emails,
        "Cars and Plates": cars_and_plates
    }

    print()

    profcheck(data)

    print()

    filecreate(filename, data)

if __name__ == "__main__":
    main()
