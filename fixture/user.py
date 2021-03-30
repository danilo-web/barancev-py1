class UserHelper:

    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
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

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.implicitly_wait(2)  # is it needed?
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[text()='Mike']/..//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[text()='Mike']/..//*[@title='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("changed_name_here")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("changed_name_here")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("changed_name_here")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
