import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('form_results.csv')
formData = pd.DataFrame(df)

#Showing how many people have hobbies
df['Hobbies'].hist(align = 'mid', color = 'red', edgecolor = 'black', label = 'Do they have hobbies?')
plt.xlabel('Do they have hobbies?')
plt.ylabel('Student Count')
plt.show()

#Showing the amount of sleep, hobbying, and studying students get done
sleep_column = df['Sleep Hours'].tolist()
work_column = df['Study Hours'].tolist()
hobby_column = df['Hobby Hours'].tolist()
sleep_sum = sum(sleep_column)
work_sum = sum(work_column)
hobby_sum = sum(hobby_column)
categories = ['Sleep', 'Study', 'Hobby']
values = [sleep_sum, work_sum, hobby_sum]
plt.barh(categories, values,height = 0.5, left = 5, color = 'green', edgecolor = 'black', align = 'center')
plt.show()

#Shows students grades based on if they think they have a work life balance
grade_names = ['A', 'B', 'C', 'D', 'F']
yes_list = []
kind_list = []
no_list = []
def work_life():
    if df['Work-Life Balance'] == 'Yes':
        yes_list.append(df['Grades'])

work_life()
print(yes_list)

