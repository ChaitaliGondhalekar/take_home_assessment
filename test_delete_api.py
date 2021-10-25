import requests
import random
from helper_functions import get_random_valid_pet_id

# Pretest Preparation phase: prepare test database with some entries


url = "http://chaitali.tj.dev.do.kasten.io/api/pets"


def test_deletePet():
    pet_id = get_random_valid_pet_id()
    response = requests.delete(url + "/" + str(pet_id))
    # confirm that it is deleted
    assert response.status_code == 204


def test_delete_non_existent_pet():
    pet_id = get_random_valid_pet_id()
    response = requests.delete(url + str(pet_id))
    assert response.status_code == 404
    # lock down message as well

# Post-test phase: restore database to pretest state
