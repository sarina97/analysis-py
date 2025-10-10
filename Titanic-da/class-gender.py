import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')
print(df.describe())
print('..........................')
df.info()

gender_class=df.groupby(['Pclass','Sex'])['PassengerId'].count().reset_index()
print(gender_class)

classes = sorted([int(c) for c in df['Pclass'].unique()])

class_labels = {
    1: 'First Class',
    2: 'Mid Class',
    3: 'Economy'
}

male_count = gender_class[gender_class['Sex'] == 'male']['PassengerId'].values
female_count=gender_class[gender_class['Sex']=='female']['PassengerId'].values

x = range(len(classes))
bar_width = 0.35

plt.figure(figsize=(8,5))

plt.bar([i - bar_width/2 for i in x], male_count, width=bar_width, label='Male')
plt.bar([i + bar_width/2 for i in x], female_count, width=bar_width, label='Female')

plt.title('Number of Male/Female in Each Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.xticks(x,[class_labels[c]for c in classes],fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
