# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from user import User


class AddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        self.open_homepage("http://localhost/addressbook/index.php")
        self.login(username="admin", password="secret")
        self.create_user(User(name="Mike", last_name="Sboev", phone="5555555"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_user(self, user):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.last_name)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.phone)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, homepage_url):
        wd = self.wd
        wd.get(homepage_url)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
