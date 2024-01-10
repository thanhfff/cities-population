import pandas as pd
data = pd.read_csv(filepath_or_buffer="cities_population.csv")

# Thống kê mật độ dân số theo quốc gia
print("Task 4: ")
data['Country'] = data['Country'].str.replace('*', '')
data['Population'] = data['Population'].str.replace(',', '')
data['Population'] = pd.to_numeric(data['Population'], errors='coerce')
data = data.dropna(subset=['Population'])

data['Area KM2'] = pd.to_numeric(data['Area KM2'], errors='coerce')
data = data.dropna(subset=['Area KM2'])

df = data.groupby('Country')[['Population', 'Area KM2']].sum()

df['Density KM2'] = df['Population']/df['Area KM2']
print(df['Density KM2'])

