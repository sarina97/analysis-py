import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

print(df.describe())
print('..........................')
df.info()

survive_class = (
    df.groupby(['Pclass', 'Survived'])['PassengerId']
    .count()
    .reset_index()
)
print(survive_class)

classes = sorted(df['Pclass'].unique())
class_labels = {1: 'First Class', 2: 'Mid Class', 3: 'Economy'}

survived_count = survive_class[survive_class['Survived'] == 1]['PassengerId'].values
dead_count = survive_class[survive_class['Survived'] == 0]['PassengerId'].values

x = range(len(classes))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], survived_count, width=bar_width, color='brown', label='Survived')
plt.bar([i + bar_width/2 for i in x], dead_count, width=bar_width, color='black', label='Dead')

plt.title('Number of Survived and Dead in Each Passenger Class', fontsize=13, pad=10)
plt.xlabel('Passenger Class', fontsize=11)
plt.ylabel('Passenger Count', fontsize=11)
plt.xticks(x, [class_labels[c] for c in classes], fontsize=10)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
