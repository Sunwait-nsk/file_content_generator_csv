from datetime import datetime
import random
import pandas as pd


def date_out():
    ordinal = random.randint(737791, 738332)
    result = datetime.fromordinal(ordinal)
    return result.date()


courses_all = {}
price = {}
first_name = ['Иванов', "Петров", "Сидорова", "Конюхов", "Коченев", "Рутов"]
city = ["Красноярск", "Москва", "Санкт-Петербург", "Новосибирск", "Казань", "Омск", "Томск", "Кемерово"]
courses = ['{}{}{}{}{}'.format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
                               random.randint(0, 9), random.randint(0, 9)) for _ in range(10)]
for i, sym in enumerate(courses):
    courses_all[sym] = "Курс {}".format(i)
    price[sym] = random.randint(10000, 50000)
data_c = []
kod = []
name_c = []
price_c = []
city_c = []
first_c = []

df1 = pd.DataFrame()
for i in range(5000):
    data_c.append(date_out())
    kod.append(random.choice(courses))
    name_c.append(courses_all[kod[i]])
    price_c.append(price[kod[i]])
    city_c.append(random.choice(city))
    first_c.append(random.choice(first_name))

df2 = pd.DataFrame({'date': data_c, 'kod': kod, 'name': name_c, 'price': price_c, 'city': city_c, 'first_name': first_c})
df = df1.append(df2, ignore_index=True)

print(df)
df.to_csv('файл с данными.csv', sep=',', encoding='utf-8', index=False)

    #df = pd.DataFrame([i+1, data_c, kod, name_c, price_c, city_c, first_c], columns=['count', 'date', 'kod', 'name', 'price', 'city', 'first_name'])
