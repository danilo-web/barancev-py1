from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def create_group(self, group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_xpath("//div[@id='content']/h1").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self, homepage_url):
        wd = self.wd
        wd.get(homepage_url)

    def destroy(self):
        self.wd.quit()