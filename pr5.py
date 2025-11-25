#requests
#numpy
#pandas
#matplotlib
#Pillow
#faker
#pyfiglet
#python-dateutil
#beautifulsoup4
#schedule

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from faker import Faker
import pyfiglet
from dateutil import parser
from bs4 import BeautifulSoup
import schedule


try:
    print("=== requests ===")
    response = requests.get("https://httpbin.org/get")
    print("Статус:", response.status_code)
    print("URL:", response.json().get("url"))
except Exception as e:
    print("Помилка в requests:", e)

try:
    print("\n=== numpy ===")
    arr = np.array([1, 2, 3, 4])
    print("Масив:", arr)
    print("Середнє:", np.mean(arr))
except Exception as e:
    print("Помилка в numpy:", e)

try:
    print("\n=== pandas ===")
    df = pd.DataFrame({
        "name": ["Alex", "Olga"],
        "age": [21, 19]
    })
    print(df)
except Exception as e:
    print("Помилка в pandas:", e)

try:
    print("\n=== faker ===")
    fake = Faker("uk_UA")
    print("Випадкове ім'я:", fake.name())
    print("Адреса:", fake.address())
except Exception as e:
    print("Помилка в faker:", e)

try:
    print("\n=== pyfiglet ===")
    print(pyfiglet.figlet_format("LAB 5"))
except Exception as e:
    print("Помилка в pyfiglet:", e)


print("\nЛаба 5 виконана успішно!")
