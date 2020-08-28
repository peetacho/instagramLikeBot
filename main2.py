#!/usr/local/bin/python3
from selenium import webdriver
from time import sleep
import random
from dotenv import load_dotenv
import os
import time
import math

load_dotenv()

# MAIN VARIABLES
POSTS_TO_LIKE = 50
un = os.getenv("USERNAME")
pw = os.getenv("PASSWORD")
tag_list = ["https://www.instagram.com/explore/tags/fitness/"]

start_time = time.time()

# add link below so ig wont suspect selenium
# https://stackoverflow.com/a/52108199/13720260


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("https://instagram.com")
        sleep(1)

        # login
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)

        self.go_to_tag()
        self.go_to_tag_9()
        self.like()

    def go_to_tag(self):
        # go to #
        self.driver.get(
            tag_list[0])
        sleep(3)

    def go_to_tag_9(self):
        # click into recent posts div element
        self.driver.find_elements_by_class_name("v1Nh3")[9]\
            .click()
        sleep(1)

    def like(self):
        try:
            self.driver.find_elements_by_css_selector("[aria-label=Like]")[0]\
                .click()
            print("like")
            sleep(1)
        except:
            print("unlike")
            sleep(1)

    def quit(self):
        self.driver.quit()
        time_elapsed = math.ceil(time.time() - start_time)
        print("time elapsed: %s seconds" % (time_elapsed))

    def on_sus_activity(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]")\
            .click()
        # print("sus found")
        sleep(1)


my_bot = InstaBot(un, pw)

for i in range(POSTS_TO_LIKE):
    try:
        my_bot.go_to_tag()
        my_bot.go_to_tag_9()
        my_bot.like()
        # print("sus not found + liked")
    except:
        my_bot.on_sus_activity()

my_bot.quit()
