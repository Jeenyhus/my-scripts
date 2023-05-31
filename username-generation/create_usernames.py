import csv
import re
import argparse

parser = argparse.ArgumentParser(description='Create usernames for learners')
parser.add_argument('data_file', type=str, help='path to the input csv file')
parser.add_argument('output_file', type=str, help='path to the output csv file')
args = parser.parse_args()

username_list = []

# opens a csv file and reads data, then assigns the data from each row to variables and removes special characters
with open(args.data_file, 'r') as file:
    learner_data = csv.DictReader(file)
    for row in learner_data:
        user_id = row['user_id']
        first_name = re.sub('[^a-zA-Z\d\s:]','',row['first_name'])
        last_name = re.sub('[^a-zA-Z\d\s:]','',row['last_name'])
        year_of_birth = row['year_of_birth']
        centre = row['centre']
        gender = row['gender']
        grade = row['grade']
        
# create usernames taking the 1st letter of their first name, first 5 letters of their last name, last 2 digits of their year of birth,
# first 3 letters of their centre and 1st letter of their gender, adding it to the username_list without any special characters.
        username = first_name[0] + last_name[0:5] + year_of_birth[-2:] + centre[0:3] + gender[0]
        username_list.append(username.lower())

# opens csv file, set the fieldnames, and write the header row. This allows the data to be stored in a structured way.
with open(args.output_file, 'w') as output_file:
    fieldnames = ['user_id', 'full_name', 'first_name', 'last_name', 'year_of_birth', 'centre', 'gender', 'grade', 'username']
    output_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    output_writer.writeheader()

# opens the csv file and iterating through the rows of data to assign each row a username from the username_list. Finally, it is writing the rows to an output file.
    with open(args.data_file, 'r') as file:
        learner_data = csv.DictReader(file)
        for index, row in enumerate(learner_data):
            row['username'] = username_list[index]
            full_name = row['first_name'] + ' ' + row['last_name']
            full_name = ' '.join(full_name.split())
            row['full_name'] = full_name
            output_writer.writerow(row)
            print(full_name + " - " + username.lower())

# Prints message to notify user that usernames have been created            
print("You have successfully created usernames!")