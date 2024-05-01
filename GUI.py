import pygame
import sys
from Heap_visualiser import *
from Patient_Database import *

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 740
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emergency Room Patient Manager")

# Colors
LIGHT_SKY_BLUE = (135, 206, 250)
NAVY_BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Fonts
heading_font = pygame.font.Font(None, 110)
font = pygame.font.Font(None, 60)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.hovered = False

    def draw(self):
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def click(self):
        if self.action:
            self.action()

#ADD PATIENT WORK 
# Flag to indicate whether a patient has been added
patient_added = False
def add_patient(hashtable,heap):
    global patient_added
    
    print("Add patient button clicked.")
    # Text variables to store user input
    input_data = {"First Name": "",
                  "Last Name": "",
                  "Severity": "",
                  "Sex": "",
                  "Age": "",
                  "Phone": "",
                  "Ward": ""}
    
    # Labels for input fields
    labels = ["First Name:", "Last Name:", "Severity:", "Sex:", "Age:", "Phone:", "Ward:"]
    
    # Input fields coordinates
    input_y = 100
    input_fields = []
    for label in labels:
        input_field = {"label": label, "text": "", "y": input_y, "active": False}
        input_fields.append(input_field)
        input_y += 70
        
    current_input_field = 0  # Index of the currently active input field
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_input_field == len(input_fields) - 1:
                        # Check if it's the last field and Enter is pressed
                        # Save data and return only if all fields are filled
                        if all(field["text"] for field in input_fields):
                            # Update input_data with the current text in each input field
                            for i, label in enumerate(input_data):
                                input_data[label] = input_fields[i]["text"]
                            add_input_list = ["Add", input_data["Severity"], input_data["First Name"], input_data["Last Name"],input_data["Sex"], input_data["Age"], input_data["Phone"], input_data["Ward"]]
                            addcheck, hashtable, heap = perform_Operation(hashtable,heap,add_input_list,wards)
                            if addcheck == False:
                                message = font.render("Patient already in database.", True, RED)
                                text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, input_fields[-1]["y"] + 100))
                                screen.blit(message, text_rect)
                                pygame.display.flip()
                                pygame.time.wait(1500)  # Wait for 1.5 seconds
                                return
                            else:
                                patient_added = True
                                message = font.render("Patient added to database.", True, RED)
                                text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, input_fields[-1]["y"] + 100))
                                screen.blit(message, text_rect)
                                pygame.display.flip()
                                pygame.time.wait(1500)  # Wait for 1.5 seconds
                                return
                            
                            # Display the message and wait for Enter
                            
                    else:
                        # Move focus to the next input field
                        current_input_field = (current_input_field + 1) % len(input_fields)
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    input_fields[current_input_field]["text"] = input_fields[current_input_field]["text"][:-1]
                else:
                    # Add character to active field text
                    input_fields[current_input_field]["text"] += event.unicode
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render input fields
        for field in input_fields:
            label = font.render(field["label"], True, BLACK)
            screen.blit(label, (SCREEN_WIDTH // 4, field["y"]))
            pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2, field["y"], SCREEN_WIDTH // 4, 50), 2)
            value = font.render(field["text"], True, BLACK)
            screen.blit(value, (SCREEN_WIDTH // 2 + 5, field["y"] + 5))
        
        # Highlight the currently active input field
        pygame.draw.rect(screen, (100, 100, 100), (SCREEN_WIDTH // 2, input_fields[current_input_field]["y"], SCREEN_WIDTH // 4, 50), 2)
        
        pygame.display.flip()


#FUnction to delete pateint

# Flag to indicate whether a patient has been deleted
patient_deleted = False
def delete_patient(hashtable, heap):
    global patient_deleted
    
    # Initialize variables
    patient_name = ""
    chosen_button = None
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # If Enter is pressed and both fields are filled, return the delete data
                    if patient_name and chosen_button:
                        delete_data = ["Delete", patient_name, chosen_button]
                        
                        print("Patient removed from ward.")
                        # Display the message and wait for 1.5 seconds
                        message = font.render("Patient deleted from the system.", True, RED)
                        text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, discharged_button_rect.bottom + 50))
                        screen.blit(message, text_rect)
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        return delete_data
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    patient_name = patient_name[:-1]
                else:
                    # Add character to patient name
                    patient_name += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check button clicks
                if deceased_button_rect.collidepoint(event.pos):
                    chosen_button = "Deceased"
                elif discharged_button_rect.collidepoint(event.pos):
                    chosen_button = "Discharged"
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render patient name input field
        patient_name_label = font.render("Enter Patient ID:", True, BLACK)
        screen.blit(patient_name_label, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 6))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 6 + 70, SCREEN_WIDTH // 3, 60), 2)
        patient_name_text = font.render(patient_name, True, BLACK)
        screen.blit(patient_name_text, (SCREEN_WIDTH // 3 + 10, SCREEN_HEIGHT // 6 + 80))
        
        # Render "Patient Status" text
        status_text = font.render("Choose Patient Status:", True, BLACK)
        screen.blit(status_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
        
        # Render buttons
        pygame.draw.rect(screen, LIGHT_SKY_BLUE, deceased_button_rect)
        pygame.draw.rect(screen, LIGHT_SKY_BLUE, discharged_button_rect)
        #render the text on the buttons
        deceased_button_text = font.render("Deceased", True, BLACK)
        discharged_button_text = font.render("Discharged", True, BLACK)
        screen.blit(deceased_button_text, (deceased_button_rect.x + 20, deceased_button_rect.y + 10))
        screen.blit(discharged_button_text, (discharged_button_rect.x + 20, discharged_button_rect.y + 10))
        # Highlight the selected button
        mouse_pos = pygame.mouse.get_pos()
        if deceased_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, deceased_button_rect)
            screen.blit(deceased_button_text, (deceased_button_rect.x + 20, deceased_button_rect.y + 10))
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
                chosen_button = "Deceased"
                delete_data = ["Delete", patient_name, chosen_button]
                hashtable,heap = perform_Operation(hashtable, heap, delete_data,wards) # Print the delete_data list
                print("Patient removed from ward.")
                # Display the message and wait for 1.5 seconds
                message = font.render("Patient deleted from the system.", True, RED)
                text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, discharged_button_rect.bottom + 50))
                screen.blit(message, text_rect)
                pygame.display.flip()
                pygame.time.wait(1500)
                return delete_data
        elif discharged_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, discharged_button_rect)
            screen.blit(discharged_button_text, (discharged_button_rect.x + 20, discharged_button_rect.y + 10))
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
                chosen_button = "Discharged"
                delete_data = ["Delete", patient_name, chosen_button]
                hashtable, heap = perform_Operation(hashtable, heap, delete_data, wards)
                print("Patient removed from ward.")
                # Display the message and wait for 1.5 seconds
                message = font.render("Patient deleted from the system.", True, RED)
                text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, discharged_button_rect.bottom + 50))
                screen.blit(message, text_rect)
                pygame.display.flip()
                pygame.time.wait(1500)
                return delete_data
        
        pygame.display.flip()

# Function to save delete patient data 
def save_deletingdata(data):
    # Save the data to the system
    pass


# Button rectangles
deceased_button_rect = pygame.Rect(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 50, 400, 60)
discharged_button_rect = pygame.Rect(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 150, 400, 60)

def find_patient(hashtable, heap):
    # Define button dimensions and positioning
    button_width = 850
    button_height = 50
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_spacing = 20
    button_y1 = (SCREEN_HEIGHT - (button_height * 2 + button_spacing)) // 2
    button_y2 = button_y1 + button_height + button_spacing
    
    # Main loop
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check button clicks
                if find_most_severe_button_rect.collidepoint(event.pos):
                    mostsevere_details_screen(hashtable,heap)
                elif find_patient_id_button_rect.collidepoint(event.pos):
                    find_thru_ID(hashtable,heap)
                
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render "Find Most Severe Patient" button
        find_most_severe_button_rect = pygame.Rect(button_x, button_y1, button_width, button_height)
        pygame.draw.rect(screen, GRAY if find_most_severe_button_rect.collidepoint(pygame.mouse.get_pos()) else LIGHT_SKY_BLUE, find_most_severe_button_rect)
        find_most_severe_button_text = font.render("Find Most Severe Patient in the System", True, BLACK)
        text_rect1 = find_most_severe_button_text.get_rect(center=find_most_severe_button_rect.center)
        screen.blit(find_most_severe_button_text, text_rect1)
        
        # Render "Find through Patient ID" button
        find_patient_id_button_rect = pygame.Rect(button_x, button_y2, button_width, button_height)
        pygame.draw.rect(screen, GRAY if find_patient_id_button_rect.collidepoint(pygame.mouse.get_pos()) else LIGHT_SKY_BLUE, find_patient_id_button_rect)
        find_patient_id_button_text = font.render("Find Patient Details through Patient ID", True, BLACK)
        text_rect2 = find_patient_id_button_text.get_rect(center=find_patient_id_button_rect.center)
        screen.blit(find_patient_id_button_text, text_rect2)
        
        pygame.display.flip()


def mostsevere_details_screen(hashtable,heap): #the screen that asks for ward number 
    # Initialize variables
    ward = ""
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # If Enter is pressed and ward name is filled, return the list ['Find', ward]
                    if ward:
                        find_data = ['Find', ward] #what we will send to our find function for most severe patient 
                        finddict, hashtable, heap = perform_Operation(hashtable, heap, find_data, wards)
                        print(finddict)#send the data to program to find
                        presentmostseveredetails(finddict)
                        return finddict
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    ward = ward[:-1]
                else:
                    # Add character to ward name
                    ward += event.unicode
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render ward name input field
        ward_label = font.render("Enter Ward Name:", True, BLACK)
        screen.blit(ward_label, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3 + 70, SCREEN_WIDTH // 3, 60), 2)
        ward_text = font.render(ward, True, BLACK)
        screen.blit(ward_text, (SCREEN_WIDTH // 3 + 10, SCREEN_HEIGHT // 3 + 80))
        
        pygame.display.flip()

 #shows the screen with the most severe patient data
def presentmostseveredetails(data):
    screen.fill(WHITE)
    
    if data is None:
        # Render the "No patients in ward empty" text
        text_surface = font.render("No patients in ward empty.", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Draw the text on the screen
        screen.blit(text_surface, text_rect)
    else:
        # Display each key-value pair of the dictionary on separate lines
        y_offset = 50
        for key, value in data.items():
            text_surface = font.render(f"{key}: {value}", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (50, y_offset)
            screen.blit(text_surface, text_rect)
            y_offset += 40

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False


def find_thru_ID(hashtable,heap):
    button_width = 300
    button_height = 60
    button_spacing = 40  # Increased spacing between buttons
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_y1 = (SCREEN_HEIGHT + 200 - (button_height * 2 + button_spacing)) // 2
    button_y2 = button_y1 + button_height + button_spacing

    all_details_button_rect = pygame.Rect(button_x, button_y1, button_width, button_height)
    specific_detail_button_rect = pygame.Rect(button_x, button_y2, button_width, button_height)  
    # Initialize variables
    patient_name = ""
    chosen_button = None
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    patient_name = patient_name[:-1]
                else:
                    # Add character to patient name
                    patient_name += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check button clicks
                if all_details_button_rect.collidepoint(event.pos):
                    chosen_button = "All Details"
                    finddata = ["Find",patient_name]
                    finddict, hashtable, heap = perform_Operation(hashtable, heap, finddata, wards)
                    alldetails_screen(finddict)
                elif specific_detail_button_rect.collidepoint(event.pos):
                    chosen_button = "Specific Detail"
                    find_specific_column(patient_name,hashtable,heap)
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render patient name input field
        patient_name_label = font.render("Enter Patient ID:", True, BLACK)
        screen.blit(patient_name_label, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 6))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 6 + 70, SCREEN_WIDTH // 3, 60), 2)
        patient_name_text = font.render(patient_name, True, BLACK)
        screen.blit(patient_name_text, (SCREEN_WIDTH // 3 + 10, SCREEN_HEIGHT // 6 + 80))
        
        # Render "Choose Option" text
        option_text = font.render("Choose Option:", True, BLACK)
        screen.blit(option_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.25))
        
        # Render buttons
        pygame.draw.rect(screen, LIGHT_SKY_BLUE, all_details_button_rect)
        pygame.draw.rect(screen, LIGHT_SKY_BLUE, specific_detail_button_rect)
        # Render the text on the buttons
        all_details_button_text = font.render("All Details", True, BLACK)
        specific_detail_button_text = font.render("Specific Detail", True, BLACK)
        screen.blit(all_details_button_text, (all_details_button_rect.x + 20, all_details_button_rect.y + 10))
        screen.blit(specific_detail_button_text, (specific_detail_button_rect.x + 20, specific_detail_button_rect.y + 10))
        # Highlight the selected button
        mouse_pos = pygame.mouse.get_pos()
        if all_details_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, all_details_button_rect)
            screen.blit(all_details_button_text, (all_details_button_rect.x + 20, all_details_button_rect.y + 10))
            
                
        elif specific_detail_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, specific_detail_button_rect)
            screen.blit(specific_detail_button_text, (specific_detail_button_rect.x + 20, specific_detail_button_rect.y + 10))
            # if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
            #     chosen_button = "Specific Detail"
                

        pygame.display.flip()
        


def alldetails_screen(data):
    # Clear the screen # have to add 2 conditions here where e . 
    screen.fill(WHITE)
    if data == None:
        sample_text = font.render("Patient Not Found.", True, BLACK)
        text_rect = sample_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(sample_text, text_rect)
    # Render the sample text
    else:
        # Display each key-value pair of the dictionary on separate lines
        y_offset = 50
        for key, value in data.items():
            text_surface = font.render(f"{key}: {value}", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (50, y_offset)
            screen.blit(text_surface, text_rect)
            y_offset += 40

    pygame.display.flip()
    
    # Wait for Enter key press to close the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Exit the function
    
        pygame.time.Clock().tick(60)  # Limit the loop to 60 frames per second

def find_specific_column(patient_name, hashtable, heap):
    # Initialize variables
    column_name = ""
    
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # If Enter is pressed and column name is filled, return the search data
                    if column_name:
                        finddata = ['Find', patient_name, column_name]
                        columndetails, hashtable, heap = perform_Operation(hashtable, heap, finddata, wards) 
                        display_column_details(columndetails)
                        return finddata
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    column_name = column_name[:-1]
                else:
                    # Add character to column name
                    column_name += event.unicode
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render column name input field
        column_name_label = font.render("Enter Column Name:", True, BLACK)
        screen.blit(column_name_label, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 4))
        columnoptions_label = font.render("Admission Date, Severity, ID, First Name, Last Name, Sex, ",True,RED)
        columnoptions_label2 = font.render("Age, Phone, Ward, Status ",True,RED)
        screen.blit(columnoptions_label,(SCREEN_WIDTH//100, SCREEN_HEIGHT//3))
        screen.blit(columnoptions_label2,(SCREEN_WIDTH//3, SCREEN_HEIGHT//2.5))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3 + 100, SCREEN_WIDTH // 3, 60), 2)
        column_name_text = font.render(column_name, True, BLACK)
        screen.blit(column_name_text, (SCREEN_WIDTH // 3 + 10, SCREEN_HEIGHT // 3 + 110))
        
        pygame.display.flip()

def display_column_details(columndetails):
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
        
        # Clear the screen
        screen.fill(WHITE)
        detail_text = font.render(str(columndetails), True, BLACK)
        screen.blit(detail_text, (50, 50))
        
        pygame.display.flip()

patient_updated = False

def update_patient(hashtable, heap):
    global patient_updated

    print("Update patient button clicked.")
    
    # Input fields coordinates
    input_y = 100
    input_fields = [
        {"label": "Patient ID:", "text": "", "y": input_y, "active": False},
        {"label": "Severity or Ward:", "text": "", "y": input_y + 70, "active": False},
        {"label": "Data to Update:", "text": "", "y": input_y + 140, "active": False}
    ]
    
    current_input_field = 0  # Index of the currently active input field
    
    # Additional details to display
    details_text = font.render("To Update: Severity or Ward?" , True, RED)
    details_text1 = font.render("Surgery,Orthopedics,Pediatrics,Cardiology,ICU" , True, RED)
   
    
    details_rect = details_text.get_rect(center=(SCREEN_WIDTH // 2, input_y + 250))
    details1_rect = details_text1.get_rect(center=(SCREEN_WIDTH // 2, input_y + 300))

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_input_field == len(input_fields) - 1:
                        # Check if it's the last field and Enter is pressed
                        # Save data and return only if all fields are filled
                        if all(field["text"] for field in input_fields):
                            update_data = ["Update", input_fields[0]["text"], input_fields[1]["text"], input_fields[2]["text"]]
                            hashtable, heap = perform_Operation(hashtable, heap, update_data,wards)
                            print(heap)
                            patient_updated = True
                            # Display the message and wait for Enter
                            message = font.render("Patient data updated.", True, RED)
                            text_rect = message.get_rect(center=(SCREEN_WIDTH // 2, input_fields[-1]["y"] + 400))
                            screen.blit(message, text_rect)
                            pygame.display.flip()
                            pygame.time.wait(1500)  # Wait for 1.5 seconds
                            return
                    else:
                        # Move focus to the next input field
                        current_input_field = (current_input_field + 1) % len(input_fields)
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    input_fields[current_input_field]["text"] = input_fields[current_input_field]["text"][:-1]
                else:
                    # Add character to active field text
                    input_fields[current_input_field]["text"] += event.unicode
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Render input fields
        for field in input_fields:
            label = font.render(field["label"], True, BLACK)
            screen.blit(label, (SCREEN_WIDTH // 4, field["y"]))
            pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2, field["y"], SCREEN_WIDTH // 4, 50), 2)
            value = font.render(field["text"], True, BLACK)
            screen.blit(value, (SCREEN_WIDTH // 2 + 5, field["y"] + 5))
        
        # Render additional details
        screen.blit(details_text, details_rect)
        screen.blit(details_text1,details1_rect)
    
        
        # Highlight the currently active input field
        pygame.draw.rect(screen, (100, 100, 100), (SCREEN_WIDTH // 2, input_fields[current_input_field]["y"], SCREEN_WIDTH // 4, 50), 2)
        
        pygame.display.flip()


    
#functions for displaying the heaps:

# Function to display text on the display ward screen
def draw_displaytext(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to display ward buttons
def draw_displaybutton(x, y, width, height, text, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    draw_displaytext(text, font, BLACK, screen, x + 10, y + 10)

# Function for when display button is clicked
# Function for when display button is clicked
def show_patient_database(hashtable, heap):
    print("Show Patient Database button clicked")
    while True:
        screen.fill(WHITE)
        draw_displaytext("Choose Ward To Display:", font, BLACK, screen, SCREEN_WIDTH//2 - 250, 50)

        # Calculate the center position for the buttons
        button_width = 250
        button_height = 100
        horizontal_padding = 20
        total_button_width = button_width * 4 + horizontal_padding * 3
        start_x = (SCREEN_WIDTH - total_button_width) // 10

        # Create buttons
        buttons = []
        button_texts = ["Surgery", "Orthopedics", "Pediatrics", "Cardiology", "ICU"]
        for i, button_text in enumerate(button_texts):
            button_x = start_x + i * (button_width + horizontal_padding)
            button_y = (SCREEN_HEIGHT - button_height) // 2
            buttons.append(pygame.Rect(button_x, button_y, button_width, button_height))
            draw_displaybutton(button_x, button_y, button_width, button_height, button_text, LIGHT_SKY_BLUE)

        selected_button = None

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, button in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        if button_texts[i] == "Surgery":
                            max_heap = heap["Surgery"]
                            draw_max_heap(max_heap)
                            # Your code for Surgery ward task here
                        elif button_texts[i] == "Orthopedics":
                            max_heap = heap["Orthopedics"]
                            draw_max_heap(max_heap)
                            # Your code for Orthopedics ward task here
                        elif button_texts[i] == "Pediatrics":
                            max_heap = heap["Pediatrics"]
                            draw_max_heap(max_heap)
                            # Your code for Pediatrics ward task here
                        elif button_texts[i] == "Cardiology":
                            max_heap = heap["Cardiology"]
                            draw_max_heap(max_heap)
                            # Your code for Cardiology ward task here
                        elif button_texts[i] == "ICU":
                            max_heap = heap["ICU"]
                            draw_max_heap(max_heap)
                            # Your code for ICU ward task here
                        
                        selected_button = ["Display", button_texts[i]]

        # Button hover effect
        for i, button in enumerate(buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
                draw_displaybutton(button.x, button.y, button.width, button.height, button_texts[i], GRAY)

        pygame.display.update()

        if selected_button:
            return selected_button

        
        
#main yahan se hai 
def input_box(prompt):
    input_text = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        screen.fill(WHITE)
        draw_text(prompt, (20, 200))
        draw_text(input_text, (20, 300))
        pygame.display.flip()
    return input_text

def draw_text(text, position):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, position)

#initialising the hospital wards etc

hospital_capacity = 50
ward_capacity = 10
wards = ["Surgery","Orthopedics","Pediatrics","Cardiology","ICU"]

hashtable, heap = create_patientDatabase(hospital_capacity,ward_capacity,wards,"Patient_records.csv")
print(heap)
# print("\nICU:  ",heap["ICU"])
# print("\nSurgery:  ",heap["Surgery"])
# print("\nOrthopedics:  ",heap["Orthopedics"])
# Create buttons
button_width = 400
button_height = 80
button_margin = 30
buttons = [
    Button((SCREEN_WIDTH - button_width) / 2, 200, button_width, button_height, "Add New Patient", GRAY, LIGHT_SKY_BLUE, lambda: add_patient(hashtable, heap)),
    Button((SCREEN_WIDTH - button_width) / 2, 200 + button_height + button_margin, button_width, button_height, "Delete Patient", GRAY, LIGHT_SKY_BLUE, lambda: delete_patient(hashtable, heap)),
    Button((SCREEN_WIDTH - button_width) / 2, 200 + 2 * (button_height + button_margin), button_width, button_height, "Find Patient", GRAY, LIGHT_SKY_BLUE, lambda: find_patient(hashtable, heap)),
    Button((SCREEN_WIDTH - button_width) / 2, 200 + 3 * (button_height + button_margin), button_width, button_height, "Update Patient", GRAY, LIGHT_SKY_BLUE, lambda: update_patient(hashtable, heap)),
    Button((SCREEN_WIDTH - (button_width + 120)) / 2, 200 + 4 * (button_height + button_margin), button_width + 120 , button_height, "Display Ward Patients", GRAY, LIGHT_SKY_BLUE, lambda: show_patient_database(hashtable, heap))
]



# Main loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white color
    mouse_pos = pygame.mouse.get_pos()

    # Draw white rectangle beneath the heading
    pygame.draw.rect(screen, WHITE, (0, 60, SCREEN_WIDTH, heading_font.get_height()+20))
    heading_text = heading_font.render("Patient Manager", True, NAVY_BLUE)
    heading_rect = heading_text.get_rect(center=(SCREEN_WIDTH // 2, 110))
    screen.blit(heading_text, heading_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.click()

    for button in buttons:
        button.update(mouse_pos)
        button.draw()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
