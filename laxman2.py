import pandas as pd
data = pd.read_csv('laxman1.csv')
print(data)
total_employees = len(data)
employees_left = len(data[data['Attrition'] == 'No'])
attrition_rate = employees_left / total_employees * 100
print(f'Attrition Rate: {attrition_rate:.2f}%')
grouped_data = data.groupby(['Age','YearsAtCompany','MonthlyIncome',])['Attrition'].sum().reset_index()
grouped_data = grouped_data.rename(columns={'Attrition': 'Number left'})
max_left_row = grouped_data.loc[grouped_data['Number left'].idxmax()]
print("row with remove")
print(max_left_row)
total_people_in_group = data[(data['Age'] == max_left_row['Age']) & (data['YearsAtCompany']
== max_left_row['YearsAtCompany']) & (data['MonthlyIncome'] == max_left_row['MonthlyIncome'])].shape[0]

