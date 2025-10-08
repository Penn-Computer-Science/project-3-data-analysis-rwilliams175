import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('form_results.csv')
formData = pd.DataFrame(df)
plt.hist(formData, bins = 5)
plt.show()