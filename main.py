import datetime as dt
import pandas
import random
import os
import smtplib

my_email = "nit.kinga2@gmail.com"
password = "lejadsojcwweobxa"

now = dt.datetime.now()
current_month = now.month
current_day = now.day

birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="index")

for record in birthday_dict:
    if birthday_dict[record]["month"] == current_month and birthday_dict[record]["day"] == current_day:
        random_letter = random.choice(os.listdir("letter_templates"))
        with open(f"./letter_templates/{random_letter}") as bd_letter:
            letter_content = bd_letter.read()
        with open(f"./mails_to_send/bd_mail_for_{birthday_dict[record]['name']}", mode="w") as mail:
            letter_to_send = letter_content.replace("[NAME]", birthday_dict[record]["name"])
            mail.write(f"{letter_to_send}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_dict[record]["email"],
                msg=f"Subject: Happy Birthday!\n\n"
                    f"{letter_to_send}"
            )
