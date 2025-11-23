# Sleep-Tracker-Python-Project
A simple python project to track sleep duration and sleep quality


# Overview
This is a  Python-based *Sleep Tracking Application*that helps users record their daily sleep duration and evaluate their sleep quality.  
The program calculates total sleep hours based on user input and categorizes the sleep quality into levels like Very Poor, Poor, Good, Excellent, etc.

The project also stores every sleep entry in a text file (sleep_history.txt) so that the user can check all previous records.

# Features
- Takes sleep time and wake-up time from the user  
- Calculates total sleep hours  
- Automatically detects next-day wake-up (past midnight)  
- Decides sleep quality based on hours  
- Saves results in a file for history  
- Lets users view their sleep history  

# Technologies Used
- *Python 3*
- Built-in modules:
  - datetime

# How to Run the Project
1. Install Python 3 (if not installed).
2. Download all project files:
   - sleep_tracker.py
   - sleep_history.txt (automatically created)
3. Run the program using this command:
4. Enter:
- Sleep Time (HH:MM)
- Wake Time (HH:MM)
5. Check your results:
- Total sleep hours 
- Sleep quality  
- History option  


# How to Test the Project
- Run the program multiple times with different inputs:
- Example:
 - Sleep: 23:00, Wake: 07:00
 - Sleep: 02:00, Wake: 10:30
- Check the sleep_history.txt file to verify if entries are saved correctly.
- Try entering wake time earlier than sleep time (overnight sleep) to see next-day handling.

# Made by:
- Saksham Jain
- B.Tech CSE Core  
- VIT Bhopal University  

# Note
This project is made for the VIT Bhopal Python Course Project submission as per the official guidelines.
