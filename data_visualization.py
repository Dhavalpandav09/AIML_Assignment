import requests
import pandas as pd
import random
import matplotlib.pyplot as plt

API_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(API_URL)
data = response.json()

df = pd.DataFrame(data)

# Create fake scores
df['score'] = [random.randint(40, 100) for _ in range(len(df))]

print(df[['name', 'score']])

# Calculate average
average_score = df['score'].mean()
print("Average Score:", average_score)

# Bar chart
plt.bar(df['name'], df['score'])
plt.xticks(rotation=90)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()
