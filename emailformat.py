
import pandas as pd
import re

data = pd.read_csv("Loglens.csv") 


valid_email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def check_email_quality(email):
    if pd.isna(email): # if email is NAN
        return 'Poor'
    email = str(email).strip() # for removing extra space
    if valid_email_regex.match(email): # checking with regex expression
        return 'Good'
    elif '@' in email: # if @ present but not valid email
        return 'Bad'
    else:
        return 'Poor'


data['Email_Quality'] = data['email'].apply(check_email_quality)


data.to_excel("email_quality_output.xlsx", index=False)

print("Data is processed")
