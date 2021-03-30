# -*- coding: utf-8 -*-


def test_edit_user(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.session.login(username="admin", password="secret")
    app.user.edit()
    app.session.logout()
