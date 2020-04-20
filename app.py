import os
import json
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Bot:

    def __init__(self,name,email):
        self.name = name
        self.email = email
        # self.bot = webdriver.Firefox(executable_path='/bin/geckodriver')
        self.bot = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.bot = webdriver.ChromeOptions()
        self.bot.add_argument('--disable-extensions')
        self.bot.add_argument('--headless')
        self.bot.add_argument('--disable-gpu')
        self.bot.add_argument('--no-sandbox')
        return webdriver.Chrome(chrome_options=self.bot)

    def login(self):
        bot = self.bot
        bot.get('https://pastorchrisdigitallibrary.org/campaigns/gold/portal.php?username=cephzone3')
        time.sleep(3)
        name = bot.find_element_by_xpath("""//*[@name='fullname']""")
        email = bot.find_element_by_xpath("""//*[@name='email']""")
        name.clear()
        email.clear()
        name.send_keys(self.name)
        emailstring = self.email.split('@')
        emailoutput = emailstring[0] +'+app@'+ emailstring[1]
        email.send_keys(emailoutput)
        bot.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(3)
        bot.close()

with open('data.json') as json_file:
    data = json.load(json_file)
    i = 1
    while i < 3:
        i = i + 1
        automate = Bot(data[i]['FIRSTNAME'], data[i]['EMAIL'])
        automate.login()