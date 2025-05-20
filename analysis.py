import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Load the data
df = pd.read_csv('expense-budget.csv')

# Clean and prepare data
df['Current Modified Budget Amount'] = pd.to_numeric(df['Current Modified Budget Amount'], errors='coerce')
df = df.dropna(subset=['Current Modified Budget Amount'])

# Analysis 1: Top 10 Agencies by Budget Allocation
agency_budgets = df.groupby('Agency Name')['Current Modified Budget Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
agency_budgets.plot(kind='bar', color='skyblue')
plt.title('Top 10 Agencies by Budget Allocation (FY2017)')
plt.xlabel('Agency Name')
plt.ylabel('Budget Amount (in billions)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Analysis 2: Personal Service vs Other Than Personal Service
service_dist = df.groupby('Personal Service/Other Than Personal Service Indicator')['Current Modified Budget Amount'].sum()

plt.figure(figsize=(8, 8))
plt.pie(service_dist, labels=service_dist.index, autopct='%1.1f%%', 
        colors=['lightgreen', 'lightcoral'], startangle=90)
plt.title('Distribution of Budget: Personal vs Other Services')
plt.show()

# Analysis 3: Top 10 Expense Categories
expense_categories = df.groupby('Object Code Name')['Current Modified Budget Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
expense_categories.plot(kind='barh', color='salmon')
plt.title('Top 10 Expense Categories by Budget Amount (FY2017)')
plt.xlabel('Budget Amount (in billions)')
plt.ylabel('Expense Category')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Analysis 4: Top 10 Responsibility Centers by Budget
responsibility_centers = df.groupby('Responsibility Center Name')['Current Modified Budget Amount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
responsibility_centers.plot(kind='bar', color='lightseagreen')
plt.title('Top 10 Responsibility Centers by Budget Allocation (FY2017)')
plt.xlabel('Responsibility Center')
plt.ylabel('Budget Amount (in billions)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Additional detailed analysis code
# Calculate percentage of budget by agency
total_budget = df['Current Modified Budget Amount'].sum()
agency_percent = (agency_budgets / total_budget * 100).round(1)

# Print summary statistics
print("\nSummary Statistics:")
print(f"Total Budget: ${total_budget/1e9:.2f} billion")
print(f"Number of Agencies: {df['Agency Name'].nunique()}")
print(f"Number of Expense Categories: {df['Object Code Name'].nunique()}")
print("\nTop 5 Agencies by Budget Percentage:")
print(agency_percent.head())