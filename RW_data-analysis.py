import pandas as pd
import random
#question data
fInitial = ['A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lInitial = ['A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
hobbies = ['Yes','No','Kind of']
balance = ['Yes','No','Kind of']
grades = ['A','B','C','D','F']
initials = []

for i in range (30):
    initials.append(f"{random.choice(fInitial)} {random.choice(lInitial)}")

data = {
    "Hobbies": [random.choice(hobbies) for _ in initials],
    "Work-Life Balance": [random.choice(balance) for _ in initials],
    "Sleep Hours": [random.randint(1,10) for _ in initials],
    "Study Hours": [random.randint(1,10) for _ in initials],
    "Hobby Hours": [random.randint(1,10) for _ in initials],
    "Grades": [random.choice(grades)]
}

balance_data = pd.DataFrame(data)
print(balance_data)