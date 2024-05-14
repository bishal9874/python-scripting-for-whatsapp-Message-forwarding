"""
Created on Tue May 14 15:02:42 2024

@author: Student
"""

import pywhatkit
import time
import pyautogui
import pandas as pd

# Load the CSV file
df = pd.read_csv("B.Tech_Engagement Prog_10thMay_Run.csv")

# Loop through each phone number in the CSV

for i in range(len(df)):
    sample = df["phone_no"][i]
    phone = "+91" + str(sample)
    message = (
        "Dear Student,\n\n"
        "I hope this message finds you well! We're excited to invite you to join our engagement program, which will be held tomorrow (15-05-24) from 3 pm onwards in the hybrid mode. Those who are residing nearby Kolkata are requested to come to the university in lab 4001 SOET building and others may join through the online platform Microsoft Teams (4pm to 5pm). You'll find all the details about the meetings in given CSE departmental website link. Please be sure to check it out!\n\n"
        "Joining Link: https://www.aucse.in/more/engagement-session-2024 \n\n"
        "We look forward to your active participation. If you have any questions or concerns, feel free to contact Dr. Debashis Chakraborty at 90512 60845.\n\n"
        "Note: If you find the link is not clickable, simply reply with \"hi\" and the link will be activated.\n\n"
        "Best regards,\n"
        "Adamas University"
    )
    
    # Send the message instantly
    pywhatkit.sendwhatmsg_instantly(phone, message)
    
    # Wait for the web.whatsapp.com to load the message box
    time.sleep(7)
    
    # Click on the send button
    pyautogui.click(1050, 870, clicks=2)
    
    # Press 'Enter' to send the message
    pyautogui.press('enter')
    
    # Wait before closing the tab
    time.sleep(5)
    
    # Close the current browser tab
    pyautogui.hotkey('ctrl', 'w')
    
    # Print confirmation
    print("MESSAGE SENT TO: ", phone)