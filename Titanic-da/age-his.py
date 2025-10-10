import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')
print(df.describe())
print('..........................')
df.info()

is_not_null = df.isnull().sum()
print(is_not_null)
print('..........................')
mean_age = df['Age'].mean()
print(f"Mean age: {mean_age:.2f}")

df['Age'].fillna(mean_age)
df['Age'] = df['Age'].astype(np.float16)


plt.figure(figsize = (8,5))
df[df['Sex']=='male']['Age'].hist(alpha=.5,label='male',bins=20)
df[df['Sex']=='female']['Age'].hist(alpha=.5,label='male',bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age distribution by Gender')
plt.legend()
plt.show()



