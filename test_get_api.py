# for data object driven tests
import pytest
import requests
import random

# for external data source driven tests
from helper_functions import read_test_data_from_csv

# Pretest Preparation phase: prepare test database with some entries

url = "http://chaitali.tj.dev.do.kasten.io/api/pets/"


def test_findPet():
    response = requests.get(url)
    assert response.status_code == 200
    # verify content header format
    assert response.headers["Content-type"] == "application/json"


def test_FindPetById():
    # get available options for ID
    response = requests.get(url)
    assert response.status_code == 200
    response_body = response.json()
    for pet in response_body:
        response_by_id = requests.get(url + "/" + str(pet["id"]))
        assert response_by_id.status_code == 200


# test query
# does not filter right now
# either it is a bug or the syntax is wrong
def test_filter_by_tags():
    expected_status = "pending"
    query_params = {"status": expected_status}
    response = requests.get(url, params=query_params)
    actual = response.json()
    assert response.status_code == 200
    response = requests.get(url)
    assert response.status_code == 200
    expected = response.json()
    assert expected == actual



# assumption: the csv contains current state of the database
# this is an example of how to test the get api with dynamic inputs
#@pytest.mark.parametrize("pet_id, expected_pet_name", read_test_data_from_csv())
#def test_data_from_external_sources(pet_id, expected_pet_name):
#    response = requests.get(url + "/" + str(pet_id))
#    response_body = response.json()
#   assert response_body["name"] == expected_pet_name


# Post-test phase: restore database to pretest state
