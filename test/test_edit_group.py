# -*- coding: utf-8 -*-


def test_edit_group(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.session.login(username="admin", password="secret")
    app.group.edit()
    app.session.logout()
