import time
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

random.seed(datetime.datetime.now())

url = "https://www.wenjuan.net/s/ryIbuuX/"
driver = webdriver.PhantomJS(executable_path='/home/xu/a-project/python/dog/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

qs = ["label_58c4cd523fcf57353fd94b27",
        "label_58c4cd963fcf5735a0e15474",
        "label_58c4cda83fcf57358848acd4",
        "label_58c4cdc43fcf5735bdf83bea"]

"""
try:
    for i in range(400):
        driver.get(url)
        for q in qs:
            question = driver.find_element(By.CLASS_NAME, q)
            question.click()
        commit = driver.find_element(By.ID, "next_button")
        commit.click()
        time.sleep(random.randint(2, 4))
        driver.delete_all_cookies()
        print(i)
finally:
    driver.close()
"""

try:
    driver.get(url)
    questions = driver.find_elements(By.CLASS_NAME, "wjques")
    print(len(questions))
finally:
    driver.close()




