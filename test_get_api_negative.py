# for data object driven tests
import pytest
import requests
import random
from helper_functions import get_random_valid_pet_id


# Pretest Preparation phase: prepare test database with some entries

url = "http://chaitali.tj.dev.do.kasten.io/api/pets/"


# needs id that is not created in the preparation method
# or id that is deleted using delete method
def test_invalid_pet_id():
    response = requests.get(url)
    assert response.status_code == 200
    response_body = response.json()
    # pick a random valid pet id to delete
    pet_id = get_random_valid_pet_id()
    response = requests.delete(url + str(pet_id))
    # confirm that it is deleted
    assert response.status_code == 204
    response = requests.get(url + str(pet_id))
    # id should not be found
    assert response.status_code == 404


# Post-test phase: restore database to pretest state
# Observation for this API:
# the id is ever increasing, not possible to revert the database to pre-test state