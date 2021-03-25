# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.session.login(username="admin", password="secret")
    app.user.create(User(name="Mike", last_name="Sboev", phone="5555555"))
    app.session.logout()
