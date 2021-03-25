# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.session.login(username="admin", password="secret")
    app.user.create(User(name="Mike", last_name="Sboev", phone="5555555"))
    app.session.logout()
