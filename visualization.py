import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the dataset
df = pd.read_csv('survey lung cancer.csv')


# Bar plot for Smoking Status
plt.figure(figsize=(10, 6))
sns.countplot(x='SMOKING', data=df)
plt.title('Distribution of Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.show()

# Pie chart for Lung Cancer patients distribution
plt.figure(figsize=(8, 8))
df['LUNG_CANCER'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Lung Cancer Patients Distribution')
plt.ylabel('')
plt.show()

# Pie chart for Gender distribution
plt.figure(figsize=(8, 8))
df['GENDER'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

# Count plot for Lung Cancer
plt.figure(figsize=(8, 6))
sns.countplot(x='LUNG_CANCER', data=df)
plt.title('Count Plot for Lung Cancer')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='GENDER', y='AGE', data=df)
plt.title('Distribution of Age by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='LUNG_CANCER', y='AGE', data=df)
plt.title('Distribution of Age by Lung Cancer Status')
plt.xlabel('Lung Cancer Status')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='CHRONIC DISEASE', hue='LUNG_CANCER', data=df)
plt.title('Count of Chronic Disease by Lung Cancer Status')
plt.xlabel('Chronic Disease')
plt.ylabel('Count')
plt.show()

sns.pairplot(df, hue='LUNG_CANCER')
plt.title('Pair Plot')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['AGE'], bins=20, kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='ANXIETY', hue='SMOKING', data=df)
plt.title('Count of Anxiety by Smoking Status')
plt.xlabel('Anxiety')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='LUNG_CANCER', y='PEER_PRESSURE', data=df)
plt.title('Proportion of Peer Pressure by Lung Cancer Status')
plt.xlabel('Lung Cancer Status')
plt.ylabel('Mean Peer Pressure')
plt.show()

plt.figure(figsize=(10, 6))
sns.swarmplot(x='AGE', y='GENDER', hue='LUNG_CANCER', data=df)
plt.title('Lung Cancer Status by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Gender')
plt.show()
