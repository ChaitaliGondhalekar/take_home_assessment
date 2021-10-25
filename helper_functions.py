import csv
import requests
import random

url = "http://chaitali.tj.dev.do.kasten.io/api/pets/"


def read_test_data_from_csv():
    test_data = []
    with open("test_get_data.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header
        for row in data:
            test_data.append(row)
    return test_data


def get_random_valid_pet_id():
    response = requests.get(url)
    assert response.status_code == 200
    response_body = response.json()
    # pick a random valid pet id to delete
    pet_id = response_body[random.randint(0, len(response_body) - 1)]["id"]
    return pet_id

