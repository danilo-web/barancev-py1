# -*- coding: utf-8 -*-


def test_del_user(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.session.login(username="admin", password="secret")
    app.user.delete()
    app.session.logout()
