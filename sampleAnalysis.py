import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Load the JSON data
file_path = 'sample.json'
df = pd.read_json(file_path)

print(df.head())

# 1. Applications by Location (State)
location_counts = df['state'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=location_counts.index, y=location_counts.values, palette='viridis')
plt.title('Number of Applications by State')
plt.xlabel('State')
plt.ylabel('Number of Applications')
plt.xticks(rotation=45)
plt.show()

# 2. College Type Distribution (Tier 1, 2, 3)
college_tier_counts = df['college_type'].value_counts()
plt.figure(figsize=(7,5))
sns.barplot(x=college_tier_counts.index, y=college_tier_counts.values, palette='Set2')
plt.title('College Tier Distribution')
plt.xlabel('College Tier')
plt.ylabel('Number of Applications')
plt.show()

# 3. Affiliations (Universities)
affiliation_counts = df['affiliation'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=affiliation_counts.index, y=affiliation_counts.values, palette='coolwarm')
plt.title('Applications by University Affiliation')
plt.xlabel('University Affiliation')
plt.ylabel('Number of Applications')
plt.xticks(rotation=45)
plt.show()

# 4. Land Area Grouping (Small, Medium, Large)
df['land_size_category'] = pd.cut(df['land_area_acres'], bins=[0, 3, 7, 10], labels=['Small (0-3)', 'Medium (3.1-7)', 'Large (7.1+)'])
land_size_counts = df['land_size_category'].value_counts()
plt.figure(figsize=(7,5))
sns.barplot(x=land_size_counts.index, y=land_size_counts.values, palette='Blues')
plt.title('Colleges by Land Area (Acres)')
plt.xlabel('Land Area Category')
plt.ylabel('Number of Colleges')
plt.show()

# 5. Program Type (Tech vs Non-Tech)
program_type_counts = df['program_type'].value_counts()
plt.figure(figsize=(7,5))
sns.barplot(x=program_type_counts.index, y=program_type_counts.values, palette='Set3')
plt.title('Program Type Distribution (Tech vs Non-Tech)')
plt.xlabel('Program Type')
plt.ylabel('Number of Applications')
plt.show()

# 6. Participation in Skill Development
skill_dev_counts = df['participation_in_skill_dev'].value_counts()
plt.figure(figsize=(7,5))
sns.barplot(x=skill_dev_counts.index, y=skill_dev_counts.values, palette='autumn')
plt.title('Participation in Skill Development Programs')
plt.xlabel('Participation in Skill Development')
plt.ylabel('Number of Colleges')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()