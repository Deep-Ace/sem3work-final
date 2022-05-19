import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestPost:
    def test_model(self):
        obj = mixer.blend('accounts.Product')
        assert obj.pk == 2, 'Should create a product instance'

    def test_get_excerpt(self):
        obj = mixer.blend('accounts.Product', name='Hello World!')
        result = obj.get_excerpt(5)
        assert result == 'Hello', 'Should return first few characters'
