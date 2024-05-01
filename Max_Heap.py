def create_heap(wards, capacity):
    # Creating empty heap.
    heap={}

    # Initializing heap with wards.
    for ward in wards:
        heap[ward]=[None for i in range(capacity)]

    # Returning Initialized Heap.
    return heap

def Is_Full(heap,ward):
    # Checking if the number of elements in the heap of the ward is equal to the ward capacity.
    if length(heap,ward)==len(heap[ward]):
            return True
    
    # Heap has not reached full ward capacity.
    return False

def length(heap,ward):
    # Initializing count.
    length=0 

    # Counting Number of elements in the ward heap.
    for i in heap[ward]:
        if i!=None:
            length+=1

    # Returning Number of elements in the ward heap.
    return length
    
def peek(heap,ward): # Peeks the top most value of the Heap.
    most_severe=heap[ward][0]
    return most_severe

def insert(heap,tup):
    # Collecting ward from patient tuple containing (Severity, ward, key). 
    ward=tup[1] 

    # Checking if the ward has reached full capacity.
    if Is_Full(heap,ward)==True:
        print("No Capacity in there ward.")

    # Inserting patient in ward heap when it is not full. 
    else:
        l=length(heap,ward) # Total number of elements in the ward.

        # Finding empty slot and adding in the patient.
        for i in range(len(heap[ward])):
            if heap[ward][i]==None:
                heap[ward][i]=tup
                break
        
        # Sorting heap after addition of the patient.
        heap_sort(heap[ward])

    # Returning sorted heap's of wards.
    return heap

def remove(heap,tup):
    # Collecting ward from patient tuple containing (Severity, ward, key).
    ward=tup[1]

    # Locating and removing the patient from the heap.
    for i in range(len(heap[ward])):
        if heap[ward][i]==tup:
            heap[ward].pop(i)
            heap[ward].append(None)
            break

    # Sorting heap after removing the patient.
    heap_sort(heap[ward])

    # Returning sorted heap's of wards.
    return heap
    
def modify(heap,tup, old_Ward):
    # Collecting ward from patient tuple containing (Emergency Number, ward, key).
    ward=tup[1]

    # Collecting patient ID from patient tuple containing (Emergency Number, ward, key).
    key=tup[2]

    # Locating and updating the patient emergency Number from the heap.
    if old_Ward==ward: # Patients ward not changing
        # Finding patient.
        for i in range(len(heap[ward])):
            
            if heap[ward][i] != None:
                id=heap[ward][i][2]
                if id==key: 
                    heap[ward][i]=tup
                    index=i
                    break
        # Sorting heap after updating the patient emergency Number.
        heap_sort(heap[ward],index)
    else: # Changing patients Ward
        Old_tup=(tup[0],old_Ward,tup[2])
        remove(heap,Old_tup)
        insert(heap,tup)

    # Returning sorted heap's of wards.
    return heap

def temp_heap_sort(heap,i):#for sorting in log(n) time complexity.
    while i>=0:
        j=i
        i=(i-1)//2
        if heap[i]<heap[j]:
            heap[i],heap[j]=heap[j],heap[i]
            left=i*2+1
            right=i*2+2
            if heap[i]<heap[left]:
                heap[i],heap[left]=heap[left],heap[i]
            if heap[i]<heap[right]:
                heap[i],heap[right]=heap[right],heap[i]

# Traverses through the whole heap, since deletion can be made in between the heap as well.
# Need to add a heap sort specifically for modify and insert that has time complexity of log(n).
def heap_sort(heap): #heap of a single ward
    # Initializing the capacity of the heap.
    capacity = len(heap)

    # Sorting through all the patients in the heap according to the emergency number.
    for i in range(len(heap)):
        if heap[i]!=None: # Element is a patient and not an empty bed.
            # Collecting emergency number of parent node.
            root_Em_No=heap[i][0]

            # Calculating index of child node's.
            left=i*2+1
            right=i*2+2

            # Checking if heap following max heap properties by comparing parent and child nodes.
            if right<capacity and left<capacity:
                # Collecting emergency number of parent node.
                if heap[left]!=None:
                    left_Em_No=heap[left][0]
                if heap[right]!=None:
                    right_Em_No=heap[right][0]

                # Comparing and swapping nodes.
                if heap[right]!=None and heap[left]!=None and right_Em_No>left_Em_No:
                    heap[left],heap[right]=heap[right],heap[left]
                    left_Em_No,right_Em_No=right_Em_No,left_Em_No
                if heap[left]!=None and left_Em_No>root_Em_No:
                    heap[left],heap[i]=heap[i],heap[left]
    return heap


            #tuple format 
#tup=(EM_No, ward, key)

            # test cases
wards=["Surgery","Orthopedics","Pediatrics","Cardiology","ICU"]
capacity=10

    # testing create
#heap=create_heap(wards,capacity)
patients= [
    (10, "Pediatrics", "8e4FB470FE19bF0"),
    (1, "Surgery", "88F7B33d2bcf9f5"),
    (8, "Cardiology", "2EFC6A4e77FaEaC"),
    (9, "ICU", "baDcC4DeefD8dEB"),
    (5, "ICU", "baDcC4DeefD8dEB"),
    (2, "Orthopedics", "f90cD3E76f1A9b9"),
    (6, "Pediatrics", "bfDD7CDEF5D865B"),
    (3, "Surgery", "DbeAb8CcdfeFC2c"),
    (4, "Cardiology", "A31Bee3c201ef58"),
    (7, "Orthopedics", "bE9EEf34cB72AF7")
]
    # testing insert
#for i in patients:
#    insert(heap,i)
#print(heap)

    # testing remove
A=(8, "Cardiology", "2EFC6A4e77FaEaC")
A=(4, "Cardiology", "A31Bee3c201ef58")
#remove(heap,A)
#print(heap)
#print(len(heap[A[1]]))

    # testing modify.
B=(10, "Orthopedics", "bE9EEf34cB72AF7")
#modify(heap,B,"Orthopedics") # changing severity
#print(heap)
B=(10, "Surgery", "bE9EEf34cB72AF7")
#modify(heap,B,"Orthopedics") # changing ward
#print(heap)

    # testing peek.
C="ICU"
#D=peek(heap,C)
#print(D)