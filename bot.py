from selenium import webdriver
import os
import time

class InstagramBot:

        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.base_url = "https://www.instagram.com"
            self.driver = webdriver.Chrome('./chromedriver.exe')
            self.login()

        def login(self):
            self.driver.get('{}/accounts/login/'.format(self.base_url))
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_name('username').send_keys(self.username)
            self.driver.find_element_by_name('password').send_keys(self.password)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
            time.sleep(2)

        def nav_user(self, user):
            self.driver.get('{}/{}/'.format(self.base_url, user))

        def follow_user(self, user):
            self.nav_user(user)

            follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
            follow_button.click()

        def unfollow_user(self, user):
            self.nav_user(user)

            unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
            unfollow_button.click()

            self.driver.implicitly_wait(5)
            confirm_unfollow = self.driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")[0]
            confirm_unfollow.click()


if __name__ == '__main__':
    with open("file.txt", "r") as f:
        contents = f.readlines()
    
    username = contents[0]
    password = contents[1]

    ig_bot = InstagramBot(username, password)

    #ig_bot.nav_user('karimbenzema')
    ig_bot.follow_user('karimbenzema')