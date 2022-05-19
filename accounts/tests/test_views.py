from django.test import RequestFactory
from .. import views


class TestUserHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.UserHomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'
