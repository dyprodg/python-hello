import pytest
import requests

from main import fetch_data

# Mock URL und Daten für Tests
MOCK_URL = 'https://jsonplaceholder.typicode.com/posts'
MOCK_DATA = [
    {'userId': 1, 'id': 1, 'title': 'Test Title 1', 'body': 'Test Body 1'},
    {'userId': 2, 'id': 2, 'title': 'Test Title 2', 'body': 'Test Body 2'}
]

# Testfunktion für fetch_data
def test_fetch_data(monkeypatch):
    # Mock-Anfrage-Funktion, die MOCK_DATA zurückgibt
    def mock_get(*args, **kwargs):
        class MockResponse:
            @staticmethod
            def json():
                return MOCK_DATA
        return MockResponse()

    # Patch 'requests.get' mit unserer Mock-Funktion
    monkeypatch.setattr(requests, "get", mock_get)

    # Führe die fetch_data Funktion aus
    result = fetch_data(MOCK_URL)

    # Überprüfe, ob das Ergebnis unseren Mock-Daten entspricht
    assert result == MOCK_DATA