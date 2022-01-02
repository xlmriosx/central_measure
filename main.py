import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot

df = pd.read_csv('cars.csv')

print(df.head())

print(df['price_usd'].mean())

print(df['price_usd'].median())

df['price_usd'].plot.hist(bins=20)
plot.ylabel('Frequency')
plot.xlabel('Price')
plot.title('Histogram: Freq vs Price')
plot.show()

sns.displot(df, x='price_usd', hue='manufacturer_name')
plot.ylabel('Frequency')
plot.xlabel('Price')
plot.title('Calor - Histogram: Freq vs Price')
plot.show()

# sns.displot(df, x='price_usd', hue = 'engine_type', multiple='stack')
sns.displot(df, x="price_usd", hue="engine_type")
plot.ylabel('Frequency')
plot.xlabel('Engine type')
plot.title('Histogram: Freq vs Engine type')
plot.show()

print(df.groupby('engine_type').count())

Q7_df = df[(df['manufacturer_name']=='Audi') & (df['model_name']=='Q7')]
sns.histplot(Q7_df, x='price_usd', hue = 'year_produced')
plot.show()


