import pandas as pd
import random
#question data
fInitial = ['A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lInitial = ['A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
hobbies = ['Yes','No','Kind of']
balance = ['Yes','No','Kind of']
grades = ['A','B','C','D','F']
#initials = []

for i in range (30):
    #initials.append(f"{random.choice(fInitial)} {random.choice(lInitial)}")
    continue

data = {
    #"Initials": initials,
    "Hobbies": [random.choice(hobbies) for _ in range(30)],
    "Work-Life Balance": [random.choice(balance) for _ in range(30)],
    "Sleep Hours": [random.randint(1,10) for _ in range(30)],
    "Study Hours": [random.randint(1,10) for _ in range(30)],
    "Hobby Hours": [random.randint(1,10) for _ in range(30)],
    "Grades": [random.choice(grades)for _ in range(30)]
}

balanceData = pd.DataFrame(data)
print(balanceData)
balanceData.to_csv('junk_data.csv', index=False)