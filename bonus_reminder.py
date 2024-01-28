import pandas as pd
import datetime
import smtplib
from email.message import EmailMessage


def send_bonus_reminders(file_path, email, password):
    # Read the .xlsx file
    data = pd.read_excel(file_path)

    # Current date
    today = datetime.datetime.now().date()

    # Iterate over each row
    for index, row in data.iterrows():
        hire_date = pd.to_datetime(row['Hire Date'])
        months_until_bonus = row['Months Until Bonus']

        # Calculate bonus date
        bonus_date = hire_date + pd.DateOffset(months=months_until_bonus)

        # Check if today's date is the bonus date
        if bonus_date.date() == today:
            name = row['Name']

            # Prepare email
            msg = EmailMessage()
            msg.set_content(f"{name} is now available to receive a bonus")
            msg['Subject'] = 'Bonus Reminder'
            msg['From'] = email
            msg['To'] = email

            # Send email using Gmail
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(email, password)
                    smtp.send_message(msg)
                print(f"Reminder sent for {name}")
            except Exception as e:
                print(f"Error sending email for {name}: {e}")


# Usage example:
# send_bonus_reminders('path_to_your_excel_file.xlsx', 'your_email@gmail.com', 'your_password')


def main():
    # Set the file path, your email, and password
    file_path = 'bonus_dates.xlsx'
    email = 'email@gmail.com'
    password = 'password'

    # Call the function to send bonus reminders
    send_bonus_reminders(file_path, email, password)


if __name__ == "__main__":
    main()
