# Task 1: Visualize Distribution of Age and Gender in a Population
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data
np.random.seed(42)  # for reproducibility

n = 200
ages = np.random.normal(loc=35, scale=10, size=n).astype(int)  # normal distribution around 35 years
genders = np.random.choice(['Male', 'Female'], size=n, p=[0.5, 0.5])  # 50-50 gender split

# Create DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Gender': genders
})

# Show head
print("Sample Data:")
print(df.head())

# Plot Histogram of Age
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot Bar Chart of Gender
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Gender', hue='Gender', palette='Set2', legend=False)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()