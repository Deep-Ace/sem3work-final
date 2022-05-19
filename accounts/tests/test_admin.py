import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer
from .. import admin
from .. import models
pytestmark = pytest.mark.django_db


class TestProductAdmin:
    def test_excerpt(self):
        site = AdminSite()
        product_admin = admin.ProductAdmin(models.Product, site)

        obj = mixer.blend('accounts.Product', name="Hello World")
        result = product_admin.excerpt(obj)
        assert result == "Hello", 'Should return first few characters'
