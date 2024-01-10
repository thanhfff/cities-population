import pandas as pd
data = pd.read_csv(filepath_or_buffer="cities_population.csv")

#sap xep in ra 10 thanh pho co dan so lon nhat va 10 thanh pho co dan so nho nhat
print("Task 1: ")
new_data = data[["City", "Population"]]
new_data['Population'] = new_data['Population'].str.replace(',', '').astype(int)
sorted_data = new_data.sort_values(by='Population', ascending=False)
print(sorted_data.head(10))
print(sorted_data.tail(10))

#in ra ten cac quoc gia co toi thieu 3 thanh pho
print("Task 2: ")
new_data_1 = data[['Country']]
city_count_by_country = new_data_1['Country'].value_counts()
result = city_count_by_country[city_count_by_country >= 3]
print(result)

# In ra các thành phố có dân số & diện tích đều nằm trong Top 20
print("Task 3: ")
#tao top 20 population
df1 = data[['Population', 'City']]
df1['Population'] = df1['Population'].str.replace(',', '').astype(int)
df1['Population'] = pd.to_numeric(df1['Population'], errors='coerce')
df1 = df1.dropna(subset=['Population'])
df1_sorted = df1.sort_values(by='Population', ascending=False)
df1_top20 = df1_sorted.head(20)
#tao top 20 area
df2 = data[['Area KM2', 'City']]
df2['Area KM2'] = pd.to_numeric(df2['Area KM2'], errors='coerce')
df2 = df2.dropna(subset=['Area KM2'])
df2_sorted = df2.sort_values(by='Area KM2', ascending=False)
df2_top20 = df2_sorted.head(20)
#Inner Join 2 top 20
df = pd.merge(df1_top20, df2_top20, on='City', how='inner')
print(df)