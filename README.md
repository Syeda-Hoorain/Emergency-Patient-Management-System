# Emergency-Patient-Management-System

## Overview
The Emergency Patient Manager is a comprehensive application developed to streamline patient management in hospital emergency wards. The project utilizes various data structures and modules to efficiently manage patient records, prioritize emergency cases, and visualize ward occupancy. It employs a modular approach, with separate Python files for different functionalities, promoting organization and ease of maintenance.

## Features
- **Patient Records Management:** Utilizes a hashtable data structure to maintain hospital records, ensuring efficient storage and retrieval of patient information.
- **Emergency Patient Prioritization:** Implements a max-heap data structure to manage emergency patients in hospital wards, allowing for quick access to the most critical cases.
- **Real-time Data Handling:** Reads, writes, and appends patient records in CSV files in real-time, ensuring data integrity and accuracy.
- **Date and Time Management:** Utilizes the datetime library to incorporate real-time date additions in patient records, facilitating accurate timestamping.
- **Separate CSV Files:** Maintains separate CSV files for current and old patient records, enabling easy retrieval and management of historical data.
- **GUI Interface:** Features a Pygame-based graphical user interface for user interaction, enhancing usability and visual appeal.
- **Visualization:** Utilizes matplotlib.pyplot and networkx to visualize ward occupancy and build the max-heap structure within the GUI, providing users with a clear overview of emergency cases and ward status.

## Modular Structure
- **Main File (GUI):** Runs the GUI interface and imports other Python files for seamless integration.
- **Max_Heap:** Implements the max-heap data structure for prioritizing emergency patients and performing operations like insertion, deletion, modification, and peeking.
- **Heap_Visualization:** Utilizes matplotlib.pyplot and networkx to visualize the max-heap structure within the GUI, enhancing user understanding of ward occupancy and emergency case prioritization.
- **Hashtable:** Manages hospital records using a hashtable data structure, ensuring efficient storage and retrieval of patient information.
- **Patient_Records (Operations):** Handles all operations related to patient records, including reading, writing, and updating CSV files, as well as interfacing with the hashtable and max-heap modules.
- **GUI:** The main file responsible for running the graphical user interface, importing the operations module, and facilitating user interaction.

## Testing and Bug Handling
- **Individual Module Testing:** Includes testing within each module to identify and rectify bugs, ensuring the reliability and stability of the application.
- **Operation.csv:** Contains operations and corner case test cases to test the Patient_Records.py module independently, facilitating bug detection and resolution without needing to run the GUI.

## Future Enhancements
- **Optimized Heap Sort:** Currently, the project employs a heap sort with O(n) time complexity. Future enhancements will involve implementing separate heap sorts for insertion and modification operations, achieving O(log n) capacity for more efficient sorting.
- **Enhanced User Interface:** Continuously improve the GUI interface for better user experience and accessibility, incorporating user feedback and usability testing.

## Additional Future Enhancements

1. **User Authentication and Access Control:** Implement user authentication mechanisms to restrict access to sensitive patient data based on user roles and permissions. This would enhance security and ensure compliance with privacy regulations.

2. **Search and Filter Functionality:** Introduce advanced search and filtering capabilities within the GUI to allow users to quickly locate specific patient records based on various criteria such as name, date of admission, medical condition, etc.

3. **Automated Notifications:** Incorporate automated notification features to alert medical staff about critical events such as the arrival of high-priority patients, pending tasks, or changes in patient status. This could be implemented through email, SMS, or in-app notifications.

4. **Integration with External Systems:** Explore integration with external systems such as Electronic Health Records (EHR) systems or hospital management software to facilitate seamless data exchange and interoperability, reducing data duplication and manual entry.

5. **Analytics and Reporting:** Develop analytics and reporting functionalities to generate insights from patient data, such as trends in patient admissions, average wait times, resource utilization, etc. This could help hospital administrators make data-driven decisions to optimize operations and resource allocation.

6. **Mobile App Compatibility:** Extend the application's accessibility by developing a mobile app version, allowing medical staff to access patient records and perform critical functions on-the-go, enhancing flexibility and responsiveness.

7. **Multilingual Support:** Incorporate multilingual support within the GUI to cater to a diverse user base, including medical staff from different linguistic backgrounds or patients requiring translation services.

8. **Backup and Disaster Recovery:** Implement robust backup and disaster recovery mechanisms to ensure data integrity and availability in the event of system failures, natural disasters, or cyberattacks.

9. **Machine Learning Integration:** Explore the use of machine learning algorithms to analyze patient data and predict outcomes such as patient admission rates, disease progression, or resource requirements, aiding in proactive decision-making and resource planning.

10. **Continuous Performance Optimization:** Continuously monitor and optimize the performance of the application to ensure responsiveness, scalability, and reliability, especially during peak usage periods or as the dataset grows over time.

