import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Обробка даних (завантаження з файлу)
data = pd.read_csv('data.csv')

# Операції з даними:
data.info()

# Фільтрація за умовою
print("\nСпівробітники старші за 30 років:")
print(data[data['Age'] > 30])

# Обчислення середнього віку або середньої заробітної плати
print(f"\nСередній вік: {data['Age'].mean()}")
print(f"Середня заробітна плата: {data['Salary'].mean()}")

# Операції з NumPy:
arr = np.array([1, 2, 3, 4, 5])
print("\nСереднє значення масиву:")
print(np.mean(arr))

# Візуалізація даних:
plt.scatter(data['Age'], data['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Базовий аналіз:
print(f"\nКількість записів: {len(data)}")
print("Середнє значення по стовпцях:")
print(data.mean(numeric_only=True))