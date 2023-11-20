import requests
from colorama import Fore, Style, init

# Initialize colorama to support colored output on Windows
init(autoreset=True)

# Set the screen to black
print('\033[30m' + '\033[40m')

# Print the ASCII art in green color
print(Fore.GREEN + r"""   
   _____  __  __   _____    _____  _____    ____    ____   ______ 
  / ____||  \/  | / ____|  / ____||  __ \  / __ \  / __ \ |  ____|
 | (___  | \  / || (___   | (___  | |__) || |  | || |  | || |__   
  \___ \ | |\/| | \___ \   \___ \ |  ___/ | |  | || |  | ||  __|  
  ____) || |  | | ____) |  ____) || |     | |__| || |__| || |     
 |_____/ |_|  |_||_____/  |_____/ |_|      \____/  \____/ |_|  
 
 
 Created by NRTC4m0""")

# Set the screen back to the default color
print(Style.RESET_ALL)

# Prompt the user to enter the target phone number
target_phone_number = input("Enter Target Phone Number: ")

# Replace PH with the inputted phone number
phone_message = {
    'phone': target_phone_number,
    'message': '',  # Placeholder for the message
    'key': 'textbelt',
}

# Prompt the user to enter the message
target_message = input("Enter Message: ")
phone_message['message'] = target_message  # Replace MSG with the inputted text

# Print the entered values
print(f"Target Phone Number: {target_phone_number}")
print(f"Message: {target_message}")

# Ask the user if the information is correct
confirmation = input("Phone Number and Message correct? (y/n): ")

if confirmation.lower() == 'y':
    # If the user confirms, make the API request
    resp = requests.post('https://textbelt.com/text', data=phone_message)
    
    # Print the API response
    print(resp.json())
else:
    # If the user does not confirm, exit the script
    print("Stopping Script")
