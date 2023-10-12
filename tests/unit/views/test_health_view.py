from tests.test import TestCase


class TestHealthView(TestCase):
    def test_success_response(self) -> None:
        response = self.client.get('/health')

        assert 200 == response.status_code
        assert {'status': 'ok'} == response.json
