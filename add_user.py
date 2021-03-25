# -*- coding: utf-8 -*-
import pytest
from user import User
from app2 import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_homepage("http://localhost/addressbook/index.php")
    app.login(username="admin", password="secret")
    app.create_user(User(name="Mike", last_name="Sboev", phone="5555555"))
    app.logout()
