# Bonus Reminder Script

## Overview
The Bonus Reminder Script is a Python program designed to automate the process of tracking employee bonus eligibility dates. It reads an Excel file containing employee data, calculates when their bonuses are due, and sends email reminders on the specific dates when bonuses become available.

## Features
- Automatically reads employee data from an Excel file.
- Calculates bonus eligibility dates based on hire dates and months until bonus.
- Sends automated email reminders when an employee's bonus date is due.

## Requirements
- Python 3.x.
- Pandas library for data processing.
- openpyxl library for handling Excel files.
- An Excel file containing employee data in a specific format.
- A Gmail account configured to allow script access (either by enabling less secure apps or using an app-specific password).

## Excel File Format
The script expects the following columns in the Excel file:
- Employee Name.
- Hire Date in a recognizable date format (e.g., MM/DD/YYYY).
- Months Until Bonus as a numeric value.

## Setup and Installation
1. Ensure Python 3.x is installed on your system.
2. Install required Python packages: `pandas` and `openpyxl`. This can be done using `pip install pandas openpyxl`.
3. Set up your Gmail account for SMTP access. If you have 2-Step Verification enabled, generate an app-specific password. email -> security -> app passoword -> name it, save, then use that password for this script password

## Configuration
1. Edit the script to include the path to your Excel file.
2. Configure the script with your Gmail address and password or app-specific password for email notifications.

## Usage
Run the script using a Python interpreter. It can be scheduled to run daily to check for any employees whose bonus eligibility date is the current date.

## Automatic Scheduling
### For Windows:
- Use Task Scheduler to run the script at a specific time (e.g., 10 AM daily).
- Create a basic task, set the trigger, action (to run Python script), and finish the setup.

### For Unix-based Systems (Linux/macOS):
- Use `cron` to schedule the script.
- Add a cron job in the crontab file to run the script at the desired time.

## Running the Script
Use the command line or an IDE to run the script:

```
python bonus_reminder.py
```

Replace `bonus_reminder.py` with the path to your script if it's located in a different directory.

## Note
- Ensure the Excel file is correctly formatted as expected by the script.
- Check your Gmail account settings to ensure the script can send emails successfully.

## License
This script is provided "as is", without warranty of any kind. Use it at your own risk.
