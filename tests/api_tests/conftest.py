import pytest

API_KEY = "9rJtQM3L-zEnbq4xxwHN"


@pytest.fixture(scope="session")
def base_url(request):
    return "https://www.quandl.com/api/v3"


@pytest.fixture(scope="module")
def api_key(request):
    return API_KEY