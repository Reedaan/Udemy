import pandas as pd
import datetime as dt

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pd.read_csv(r"D:\Python\Python Bootcamp\Day 32\Project\birthdays.csv")
data_dict = data.to_dict()

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
day = today.day
month = today.month

print(data_dict["day"])
print(day)

if data_dict["day"] == day:
    print(day)
    


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv



# 4. Send the letter generated in step 3 to that person's email address.




