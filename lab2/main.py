import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

sns.set_theme(style="whitegrid")

csv_filename = "CarPrice_Assignment.csv"
df = pd.read_csv(csv_filename)

print("--- 1. ИСХОДНЫЕ ДАННЫЕ ---")
print(f"Размерность датасета: {df.shape[0]} строк, {df.shape[1]} столбцов\n")
print(df.head(3))

print("\n--- 2. ПРОВЕРКА ПРОПУСКОВ ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0] if missing_values.sum() > 0 else "Пропусков не обнаружено!")

plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Тепловая карта пропусков в данных")
plt.tight_layout()
plt.show()

for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object', 'string']).columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

target_col = 'price' if 'price' in df.columns else df.select_dtypes(include=[np.number]).columns[0]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df[target_col], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title(f'Распределение {target_col} (До обработки)')
sns.boxplot(x=df[target_col], ax=axes[1], color='skyblue')
axes[1].set_title(f'BoxPlot {target_col} (До обработки)')
plt.tight_layout()
plt.show()

Q1 = df[target_col].quantile(0.25)
Q3 = df[target_col].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df[target_col] = np.clip(df[target_col], lower_bound, upper_bound)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df[target_col], kde=True, ax=axes[0], color='mediumseagreen')
axes[0].set_title(f'Распределение {target_col} (После обработки)')
sns.boxplot(x=df[target_col], ax=axes[1], color='mediumseagreen')
axes[1].set_title(f'BoxPlot {target_col} (После обработки)')
plt.tight_layout()
plt.show()

print("\n--- 3. ГЕНЕРАЦИЯ ПРИЗНАКОВ И КОДИРОВАНИЕ ---")

if 'horsepower' in df.columns and 'curbweight' in df.columns:
    df['power_to_weight'] = df['horsepower'] / df['curbweight']
else:
    df['feature_ratio'] = df.iloc[:, 1] / (df.iloc[:, 2] + 1)

df['is_high_category'] = (df[target_col] > df[target_col].median()).astype(int)

print("Сгенерированы новые признаки: 'power_to_weight'/'feature_ratio' и 'is_high_category'")

cat_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True, dtype=int)
print(f"Размерность после One-Hot Encoding: {df_encoded.shape[1]} столбцов")

print("\n--- 4. МАСШТАБИРОВАНИЕ ДАННЫХ ---")
num_cols = df_encoded.select_dtypes(include=[np.number]).columns

scaler_std = StandardScaler()
df_scaled = df_encoded.copy()
df_scaled[num_cols] = scaler_std.fit_transform(df_encoded[num_cols])

scaler_minmax = MinMaxScaler()
df_normalized = df_encoded.copy()
df_normalized[num_cols] = scaler_minmax.fit_transform(df_encoded[num_cols])

print("Стандартизация и нормализация успешно выполнены!")
print("\nПример стандартизированных данных (первые 2 строки):")
print(df_scaled.head(2))