import pandas as pd
import numpy as np

pd.options.display.width = 0

import matplotlib.pyplot as plt
import seaborn as sns

fifa = pd.read_csv('fifa_data.csv')

# print(fifa.head())

# for col in fifa.columns:
#     print(col)
#
# print("\n",fifa.shape)
#
# vc= fifa['nationality'].value_counts()[0:10]
# print(vc)
#
# vc1= fifa['nationality'].value_counts()[0:10].keys()
# print(vc1)
#
# plt.figure(figsize=(8,5))
# plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color='g')
# plt.show()

# print(fifa[['short_name','wage_eur']].value_counts()[0:5])

player_sal = (fifa[['short_name', 'wage_eur']])
print(player_sal.head())
print('\n')
player_sal = player_sal.sort_values(by=['wage_eur'], ascending=False)
print(player_sal)

# plt.figure(figsize=(8,5))
# plt.bar(list(player_sal['short_name'])[0:5],list(fifa['wage_eur'])[0:5],color=['blue','yellow','red','green','orange'], edgecolor="black")
# plt.show()

a = fifa['nationality'] == 'Germany'
print(a)

nationality = fifa[fifa['nationality'] == 'Germany']
print(nationality.head(10))

print("\nby height")
height = nationality.sort_values(by=['height_cm'], ascending=False).head()
print(height)

print("\nby weight")
weight = fifa.sort_values(by=['weight_kg', 'short_name'], ascending=False).head()
print(weight)

print("\nby germany wage")
print(nationality.sort_values(by=['wage_eur'], ascending=False).head())

print("\n")
print(nationality[['short_name','wage_eur']].sort_values(by=['wage_eur'], ascending=False).head())

print("\n")
pl_shoot = fifa[['short_name','shooting']]
print(pl_shoot.sort_values(by=['shooting'],ascending=False).head())

print("\n")
defe = fifa[['short_name','defending','nationality','club']]
print(defe.sort_values(by=['defending'],ascending=False).head())


print("\n")
Manchester_City = fifa[fifa['club']=='Manchester City']
print(Manchester_City.sort_values(by=['wage_eur'],ascending=False).head())

shoot = Manchester_City[['short_name','shooting','nationality','club','wage_eur']]
print(shoot.sort_values(by=['wage_eur'],ascending=False).head())
