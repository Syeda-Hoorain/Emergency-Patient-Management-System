from HashTable import *
from Max_Heap import *
import csv

def create_patientDatabase(Hospital_capacity, ward_capacity, wards, filename):
    # Taking data input from text file
    with open(filename) as f:
        lines=f.readlines ()
    patientRecords = []
    Headings=lines.pop(0) # Extracting headings.
    Headings=Headings.strip()
    Headings=Headings.split(",")
    for line in lines :
        line = line.strip() # remove leading and trailing spaces
        tokens = line.split (',') # split the line into tokens
        data={Headings[0]:tokens[0],"Severity":int(tokens[1]), Headings[2]:tokens[2], Headings[3]: tokens[3], Headings[4]: tokens[4], Headings[5]: tokens[5], Headings[6]: tokens[6], Headings[7]: tokens[7], Headings[8]: tokens[8], Headings[9]: tokens[9]}
        patientRecords.append (data) # add the data dictionary to inputs list
    f.close()

    # Creating Hash table.
    Hashtable=create_hashtable(Hospital_capacity)

    # Creating Heap.
    Heap=create_heap(wards,ward_capacity)

    # Adding keys and values to hash table by iterating through student records
    for i in patientRecords:
        key=i["ID"]
        data=i
        Hashtable, Heap=put(Hashtable, Heap, key, data,  Hospital_capacity)

    # Returning hash table(Patient database) of under treatment patient records.    
    return Hashtable, Heap # Need to add deceased and discharged tables.
   

def perform_Operation(Hashtable, Heap, operation, wards):
    # Performing operations.
    old_patient=0 # Initializing past patients records.
    # Collecting key from inputs.
    key=operation[1]

    # Calling find operation
    if operation[0]=="Find":
        if key in wards: # If finding the most severe/emergency case in a ward. 
            ward=key
            tup=peek(Heap,ward)
            key=tup[2]
            data=get(Hashtable,key)
            print(data)
            re_write_records("Patient_records.csv",Hashtable)
            return data, Hashtable, Heap
        else:
            dict=get(Hashtable,key)
            if dict==None: # If no value returned
                print("Not found")
                return dict, Hashtable, Heap
            elif len(operation)==2: # If finding data for the key.
                print(dict)
                re_write_records("Patient_records.csv",Hashtable)
                return dict, Hashtable, Heap
            else: # If finding a particular column data for the key.
                columnName=operation[2]
                print(dict[columnName])
                re_write_records("Patient_records.csv",Hashtable)
                return dict[columnName], Hashtable, Heap

    # Calling update operation.
    elif operation[0]=="Update":
        columnName=operation[2]
        data=operation[3]
        Update(Hashtable, Heap, key, columnName, data)
        re_write_records("Patient_records.csv",Hashtable)
        return Hashtable, Heap

    # Calling Delete operation.
    elif operation[0]=="Delete": # deceased and discharged patients.
        status=operation[2] # Collecting status Deceased/Discharged.
        # Collecting old_patient in the form of dictionary along with updates hashtable and size.
        Hashtable, Heap, old_patient=delete(Hashtable, Heap, old_patient, status, key)
        Append_records("Old_Patients.csv", old_patient) # Adding deleted patient to csv file.
        re_write_records("Patient_records.csv",Hashtable) 
        return Hashtable, Heap

    # Adding new patient.
    elif operation[0]=="Add":
        Admission_date=0
        Admission_date=date(Admission_date)
        ID=generate_key(Hashtable)
        data={"Admission Date":Admission_date,"Severity":int(operation[1]),"ID":ID, "First Name":operation[2], "Last Name":operation[3], "Sex":operation[4], "Age":operation[5], "Phone":operation[6], "Ward":operation[7], "Status":"Under Treatment"}
        if in_table(data,Hashtable)==True:
            print("Patient already in the system")
            return False, Hashtable, Heap
        
        else:
            Hashtable, Heap=put(Hashtable, Heap, ID, data, Hospital_capacity)
            Append_records("Patient_records.csv",data)
            print("Patient added")
            return True, Hashtable,Heap


# Adding deleted patients to Old patients record.
def Append_records(datafile, old_patient):
    # Opening the CSV file in append mode
    with open(datafile, mode='a', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Append new data to the CSV file row by row
        writer.writerow(old_patient.values())

# Generating unique ID for new patients.
def generate_key(Hashtable): # Numerical key 
    num=Elements(Hashtable)
    return str(num)

# For rewriting the patient database with the updated data.
def re_write_records(filename, Hashtable):
    data=values(Hashtable)
    # rewriting patient database after discharging of patients.
    fieldnames = data[0].keys() if data else []
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    
    # Constant data
# Hospital capacity.
Hospital_capacity=50
# Ward capacity
ward_capacity=10
# Wards in the Hospital.
wards=["Surgery","Orthopedics","Pediatrics","Cardiology","ICU"]

    # Formats:
#data={"Admission Date":tokens[0],"Severity":tokens[1], "ID":tokens[2], "FirstName": tokens[3], "LastName": tokens[4], "Sex": tokens[5], "Age": tokens[6], "Phone": tokens[7], "Ward": tokens[8]}
#tup=(Severity,Ward,Key)








# for checking working of program without gui no need to call in case of gui

def Operations(filename, hashtable, heap, wards):
    # Taking data input from text file
    with open(filename) as f:
        lines=f.readlines ()
    operations = []
    Headings=lines.pop(0) # Extracting headings.
    for line in lines :
        line = line.strip() # remove leading and trailing spaces
        tokens = line.split (',') # split the line into tokens
        operations.append (tokens) # add the data dictionary to inputs list
    f.close()

    # Performing operations.
    for operation in operations:
        perform_Operation(hashtable, heap, operation, wards)

Hashtable, Heap=create_patientDatabase(Hospital_capacity, ward_capacity, wards, "Patient_records.csv")
#print(Hashtable)
#print(Heap)
#print(key(Hashtable))
out=Operations('Operations.csv', Hashtable, Heap, wards)
