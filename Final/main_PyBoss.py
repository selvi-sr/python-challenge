import csv
import os
input_file = os.path.join("..","Resources","employee_data.csv")
#input_file ="employee_data.csv"
output_file = os.path.join("..","Resources","employee_data_out.csv")


state_d= {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}
#initializing the variables
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []




with open(input_file) as emp_data:
    reader = csv.reader(emp_data)
    header = next(reader)
  
    for row in reader:
        emp_ids = emp_ids + [row[0]]
        
        split_name = row[1].split(" ")
        emp_first_names = emp_first_names + [split_name[0]]
        emp_last_names = emp_last_names + [split_name[1]]
        
        
       
        dob = row[2].split("-")
        year = dob[0]
        month = dob[1]
        day = dob[2]
        new_dob = f"{month}/{day}/{year}"
        emp_dobs.append(new_dob)
      
        split_ssn = list(row[3])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        masked_ssn = "".join(split_ssn)
        emp_ssns.append(masked_ssn)
        
        
        
        state_sf = state_d[row[4]]
        emp_states.append(state_sf)
        

new_emp = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)
# Write all of the election data to csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(new_emp)
