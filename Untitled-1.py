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

#Shows percentages of grades on a pie chart
s = formData['Grades']
counts = Counter(s)
d = dict(counts)
print(d)
labels = list(d.keys())
grade_count = list(d.values())
fig, ax = plt.subplots()
ax.pie(grade_count, labels = labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
plt.show()



