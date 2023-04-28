import datetime
import time
import requests

from bs4 import BeautifulSoup
import sqlite3
while True:
    connection = sqlite3.connect("test2.s13", 5)
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS firs (city TEXT, data TEXT, time TEXT, temperature TEXT);")
    connection.commit()
    response = requests.get("https://sinoptik.ua/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("div",{"class":"lSide"})
        res = soup_list[0].find("p",{"class":"today-temp"})
    print(res.text)
    cur.execute(f"INSERT INTO firs VALUES ('Ерки','{datetime.datetime.today().date()}','{datetime.datetime.today().time()}','{res.text}');")
    connection.commit()
    connection.close()
    time.sleep(1800)