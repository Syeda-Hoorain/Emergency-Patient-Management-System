from Max_Heap import *
import datetime

def create_hashtable(size): # returns tuple(list,list)
    keys_list = [None for i in range(size)] # Keys list
    data_list = [None for i in range(size)] # Data list
    hashtable = (keys_list, data_list) # Hash table
    return hashtable

def hash_function(key): #returns integer (Address)
    # Sum of ASCII value of characters
    id=int(key)
    return id

def put(hashtable, heap, key, data, Hospital_capacity): #return hashtable,size
    severity=data["Severity"] # Patient Severity.
    ward=data["Ward"] # Patient ward
        
    # If no capacity in the hospital.
    if Elements(hashtable)==Hospital_capacity:
        print("No Capacity in the hospital.")

    # If no capacity in ward.
    elif Is_Full(heap,ward)==True:
        print("No Capacity in the ward.")
    
    # If capacity in the hospital.
    else:
        # Adding new patient to Heap:
        tup=(severity, ward, key)
        heap=insert(heap,tup)

        # Adding patient to Hash table:

        # Finding address to the key.
        index = hash_function(key)
        
        # Adding the key-value pair to the hashtable

        # Address empty(no collision)
        if hashtable[0][index]==None: 
            hashtable[0][index]=key
            hashtable[1][index]=data

    return hashtable, heap


def Update(hashtable, heap, key, columnName, data): # returns Nothing, prints 'record Updated'
    # Finding address using hash function.
    add=hash_function(key)

    # Collecting old data before updates made.
    old_data=hashtable[1][add]
    old_Ward=old_data["Ward"]

    # Updating at the address found.
    hashtable[1][add][columnName]=data

    # Checking if update needed in Heap.
    if columnName=="Severity" or columnName=="Ward":
        info=hashtable[1][add] # Collecting data of patient from the hash table.
        if columnName=="Severity": # Collecting Severity and ward if severity updating.
            severity=int(data) # Collecting Patient severity.
            ward=old_Ward # Collecting Patient ward
            hashtable[1][add][columnName]=severity # updating integer severity.
        else: # Collecting Severity and ward if ward updating.
            ward=data# Collecting Patient ward
            severity=info["Severity"] # Collecting Patient severity.
        
        tup=(severity, ward, key) # Initializing new tuple
        modify(heap,tup, old_Ward) # Modifying/updating tuple in the ward's heap.

    print("record Updated")
    
def get(hashtable,key): # returns dictionary
    # Finding address using hash function.
    add=hash_function(key)

    # Getting the data at the address found.
    data=hashtable[1][add]
    return data

def delete(hashtable, heap, old_patients, status, key): #returns hashtable, size, prints a msg  'Item Deleted'
    # Finding address using hash function.
    add=hash_function(key)

    # Collecting leaving patients data and adding leaving date to the data.
    info=hashtable[1][add].copy() # Collecting data of patient from the hash table.
    formatted_date=0 # Initializing real-time date to send as parameter
    info["Leaving date"]= date(formatted_date) # Adding in date when patient is removed from records.
    info["Status"]=status

    # Deleting item from Heap.
    severity=info["Severity"] # Collecting Patient Severity.
    ward=info["Ward"] # Collecting Patient ward
    tup=(severity, ward, key) # Initializing tuple
    remove(heap,tup) # Removing tuple from ward.

    # deleting severity and adding data to Old patients list.
    del info["Severity"]
    old_patients=info

    # Deleting item from Hashtable.
    hashtable[1][add]["Status"]=status

    print("Item Deleted")

    return hashtable, heap, old_patients

def in_table(data,hashtable):
    # Storing data without ID for comparision.
    d=data.copy()
    del d["ID"]
    del d["Admission Date"]
    #del d["Status"]

    # Comparing data with all details in hashtable.
    for item in hashtable[1]:
        if item!=None and item!="#":
            info=item.copy()
            del info["ID"]
            del info["Admission Date"]
            #del info["Status"]
            # If patient already in data base.
            if info==d:
                return True
            
    # Patient not in database.
    return False


# Helper functions:

# Helper function to get real-time date.
def date(formatted_date):
    # Getting the current date
    current_date = datetime.date.today()

    # Convertting the date to desired format.
    formatted_date = current_date.strftime("%d/%m/%Y")  # Format: DD/MM/YYYY

    return formatted_date

# Helper function to give number of elements in hashtable.
def Elements(hashtable): #returns size of hashtable as integer
    num=0
    for i in hashtable[0]:
        if i!=None:
            num+=1
    return num

# Makes a list of all the values in the hashtable without none.
def values(H):
    vals=[]
    for i in H[1]:
        if i!=None:
            vals.append(i)
        if i==None:
            return vals
    return vals

# Helper function to check if number is prime.
def isprime(n): # Returns True if number is a prime else returns False.
    # Does not check for 1,2,3 since we know this function will be called for values >= 7.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True