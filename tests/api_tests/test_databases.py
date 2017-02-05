import requests


def test_database_api_returns_a_list_of_databases(base_url):
    databases = requests.get("{}/databases".format(base_url)).json()["databases"]
    assert type(databases) == list, "Databases api does not return a list"
    assert len(databases) > 0, "List of databases is empty"


def test_user_gets_data_when_datatset_is_used(base_url):
    dataset = requests.get("{}/datasets/GOOG/NASDAQ_AAPL/data.json".format(base_url)).json()["dataset_data"]
    assert len(dataset["data"]) > 0, "Dataset contains no data"


def test_get_wiki_with_valid_key(api_key, base_url):
    dataset = requests.get("{}/datasets/WIKI/FB.json".format(base_url), data={'api_key': api_key}).json()["dataset"]
    assert len(dataset.get("data")) > 0, "Dataset is empty when it shouldn't be"
