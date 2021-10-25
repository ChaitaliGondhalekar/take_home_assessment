import requests

# Pretest Preparation phase: prepare test database with some entries

url = "http://chaitali.tj.dev.do.kasten.io/api/pets"
test_data = {'name': 'Gecko21', 'status': 'available'}  # cannot predict ID


def test_addPet():
    response = requests.post(url, json=test_data)
    assert response.status_code == 200
    # verify content header format
    assert response.headers["Content-type"] == "application/json"
    response_body = response.json()
    assert response_body["name"] == test_data["name"]


test_data = {'name': 'toad', 'status': 'available'}


def test_duplicate():
    entry_1 = requests.post(url, json=test_data)
    assert entry_1.status_code == 200
    entry_2 = requests.post(url, json=test_data)
    assert entry_2.status_code == 200
    # verify content header format
    assert entry_2.headers["Content-type"] == "application/json"
    entry_2_body = entry_2.json()
    assert entry_2_body["name"] == test_data["name"]


# only json input is allowed
def test_wrong_format():
    entry_1 = requests.post(url, test_data)
    assert entry_1.status_code == 415

# Post-test phase: restore database to pretest state
