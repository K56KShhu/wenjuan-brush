import time
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

random.seed(datetime.datetime.now())

driver = webdriver.PhantomJS(executable_path='/home/xu/a-project/python/dog/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

times = 300
url = "https://www.wenjuan.net/s/ryIbuuX/"

try:
    for i in range(300):
        driver.get(url)
        questions = driver.find_elements(By.CLASS_NAME, "wjques")
        for question in questions:
            answers = question.find_elements(By.CLASS_NAME, "option_label")
            lucky_answer = answers[random.randint(0, len(answers) - 1)]
            lucky_answer.click()
        commit = driver.find_element(By.ID, "next_button")
        commit.click()
        time.sleep(random.randint(2, 4))
        driver.delete_all_cookies()
        print(i)
finally:
    driver.close()




