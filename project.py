import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)
days = np.arange(1, 366)
temperatures = 10 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 2, 365)
precipitation = np.random.uniform(0, 10, 365)
humidity = np.random.uniform(40, 80, 365)

mean_temp = np.mean(temperatures)
hot_days = days[temperatures > mean_temp + 5]
cold_days = days[temperatures < mean_temp - 5]

plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, label='Температура', color='blue')
plt.axhline(mean_temp, color='red', linestyle='--', label=f'Средняя температура {mean_temp:.2f}C')
plt.scatter(hot_days, temperatures[temperatures > mean_temp + 5], color='red', label='Аномально жаркие дни')
plt.scatter(hot_days, temperatures[temperatures < mean_temp - 5], color='cyan', label='Аномально хододные дни')
plt.xlabel('День года')
plt.ylabel('Температура {C}')
plt.title('Температура в течение года')
plt.legend()
plt.grid()
plt.show()

coeffs = np.polyfit(days, temperatures, 3)
trend_poly = np.poly1d(coeffs)
trend_temps = trend_poly(days)

plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, label='Температура', alpha=0.5)
plt.plot(days, trend_temps, label='Тренд(полином 3-й степени)', color='red', linewidth=2)
plt.xlabel('День года')
plt.ylabel('Температура (C)')
plt.title('Температурный тренд')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(days,precipitation, label='Осадки (мм)', color='blue', alpha=0.6)
plt.xlabel('День года')
plt.ylabel('Осадки (мм)')
plt.title('Осадки в течении года')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(days, humidity, label='Влажность (%)', color='pink')
plt.xlabel('День года')
plt.ylabel('Влажность (%)')
plt.title('Влажность в течении года')
plt.legend()
plt.grid()
plt.show()

correlation_temp_humitity = np.corrcoef(temperatures, humidity)[0, 1]
print(f'Корреляция между температурой и влажностью: {correlation_temp_humitity:.2f}')