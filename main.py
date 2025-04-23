from datetime import date
import pandas as pd
from send_email import send_email


SHEET_ID = "1QPVDGZ9Psqe3Oeb74unJwi0XY-VJXUeVUL4BI5P1NGo"  # CHANGE IT FOR NEW SHEET
SHEET_NAME = "htmldata"  # CHANGE IT FOR NEW SHEET
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates) #dayfirst=True
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if isinstance(row["reminder_date"], pd.Timestamp):
            reminder_date = row["reminder_date"].date()
        else:
            print(f"Invalid reminder_date: {row['reminder_date']}")
            continue

        if (present >= reminder_date) and (row["status"] == "no"):
            send_email(
                subject=row["subject"],
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y")
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)