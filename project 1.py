import pandas as pd
import matplotlib.pyplot as plt

# 1. Məlumatın Yüklənməsi və Baxış

path = r"C:\Users\Computer\Downloads\sales_data_sample.csv"
df = pd.read_csv(path, encoding='latin1')

print("--- Data Shape (Ölçüsü) ---")
print(df.shape)  # sətir və sütun sayı

print("\n--- Column Names (Sütun Adları) ---")
print(df.columns.tolist())

print("\n--- Data Types (Məlumat Tipləri) ---")
print(df.dtypes)


# 2. Məlumatın Təmizlənməsi

# ORDERDATE sütununu datetime formatına çevirmək
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Missing values-ın bütün sütunlar üzrə yoxlanılması
print("\n--- Missing Values Before Cleaning (bütün sütunlar) ---")
print(df.isnull().sum())

# Boş xanaların "Unknown" ilə doldurulması
# (TERRITORY də əlavə olundu - bu sütunda da 1074 boş xana var idi)
cols_to_fill = ['ADDRESSLINE2', 'STATE', 'POSTALCODE', 'TERRITORY']
for c in cols_to_fill:
    df[c] = df[c].fillna('Unknown')

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# Duplikat sətirlərin yoxlanılması
duplikat_sayi = df.duplicated().sum()
print(f"\nDuplikat sətirlərin sayı: {duplikat_sayi}")


# 3. Statistik Göstəricilər

print("\n--- Summary Statistics for Numeric Columns ---")
print(df.describe())

print("\n--- Value Counts for STATUS (say) ---")
print(df['STATUS'].value_counts())

print("\n--- Value Counts for STATUS (faiz, %) ---")
print(df['STATUS'].value_counts(normalize=True).round(3) * 100)

print("\n--- Value Counts for YEAR_ID ---")
print(df['YEAR_ID'].value_counts().sort_index())

print("\n--- Value Counts for PRODUCTLINE ---")
print(df['PRODUCTLINE'].value_counts())


# 4. Vizuallaşdırma və Qrafiklər

# Qrafik 1: SALES sütununun histogramı
plt.figure(figsize=(10, 5))
plt.hist(df['SALES'], bins=30, color='skyblue', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('sales_histogram.png', dpi=120)
plt.show()

# Qrafik 2: İllərə görə sifariş sayı (bar chart il')
plt.figure(figsize=(10, 5))
order_counts_by_year = df['YEAR_ID'].value_counts().sort_index()
order_counts_by_year.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Order Count by YEAR_ID')
plt.xlabel('Year')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('orders_by_year.png', dpi=120)
plt.show()


# 5. Business Insights

print("""
--- BUSINESS INSIGHTS ---
1. Sifarişlərin 92.7%-i Shipped statusundadır, cəmi 2.1%-i Cancelled.
2. Classic Cars ən güclü məhsul xəttidir: 967 sifariş, 3.92M satış.
3. 2004-cü il pik ildir: 1345 sifariş ; 2005-in az sayı natamam il məlumatı ola bilər.
4. Large sifarişlərin orta satışı (8294) Small sifarişlərdən (~2062) 4 dəfə çoxdur;
 ABŞ ən böyük bazardır (3.6M).
""")