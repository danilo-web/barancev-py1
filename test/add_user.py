# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.app2 import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_home_page("http://localhost/addressbook/index.php")
    app.login(username="admin", password="secret")
    app.create_user(User(name="Mike", last_name="Sboev", phone="5555555"))
    app.logout()
