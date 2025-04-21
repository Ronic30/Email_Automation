# Email_Automation
EMAIL_AUTOMATION using Python, where you can send a reminder using the Python script.

How it Works :
  1. Fetch the data from a spreadsheet by converting the spreadsheet into a CSV file to use it in a Python script.
  2. Spreadsheet includes attributes like: name, project, due_date,
  3. We'll make a variable named present_date where we store the present date.
  4. So when a date is passed, it automatically sends the email to the user as a reminder.

How to use it:
  1. First step is to install essential libraries like pandas, datetime, pymail, and smtplib(simple mail transfer protocol).
  2. Create a .env file to store the Owner's Email and Password.
  3. Create a .gitignore file.
  4. Create a send_email.py file that stores:
       - The email server and port for the Gmail ID and the read environment variable.
       - The email contents and structures.
       - Error-handling statements.
  5. Create a main.py file: the backbone of our email automation process for sending the reminder email. It stores:
       1. Google Sheets information, like Sheet Name and Sheet ID, converts the Google Sheet into a .csv file.
       2. A function including:
            - A variable to store the present date and import the reminder date from the CSV.
            - Then we'll compare the present date and the reminder date.
            - And if the present date is greater than or equal to the reminder date, the Email is automatically sent to the respective user.
       
