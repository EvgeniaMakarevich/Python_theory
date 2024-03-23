import pytest
import requests


base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'

@pytest.fixture(scope="module")
def get_token():
    payload = {
    "username" : "admin",
    "password" : "password123"
}
    result = requests.post(auth_url, json = payload)
    result_data = result.json()
    token = result_data['token']
    yield token


@pytest.fixture(scope="module")
def get_booking_id():
    payload = {
        "firstname": "Jane",
        "lastname": "Makarevich",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200


def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200

    expected_keys = {
    "firstname": "Jim",
    "lastname": "Jackson",
    "totalprice": 986,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2022-03-03",
        "checkout": "2023-06-16"
    }}
    for key in expected_keys:
        assert key in response_data.keys()


def test_create_booking():
    global booking_id

    payload = {
    "firstname" : "Jane",
    "lastname" : "Makarevich",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-01-01",
        "checkout" : "2024-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(base_url, json = payload)
    print(response.json()['bookingid'])
    assert response.status_code == 200
    booking_id = response.json()['bookingid']




def test_get_specific_booking():
    result = requests.get(f'{base_url}/926')
    expected_keys = {
        "firstname": "Jane",
        "lastname": "Makarevich",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    result_data = result.json()
    print(result_data)
    for key, value in expected_keys.items():
        assert key in result_data.keys()
        assert result_data[key] == value



@pytest.mark.smoke
def test_update_booking(get_token, get_booking_id):
    payload = {
        "firstname": "Jane_1",
        "lastname": "Makarevich",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Dinner"
    }
    token = {"Cookie": f"token = {get_token}"}
    response = requests.put(f'{base_url}/{get_booking_id}', json = payload, headers = token)
    assert response.status_code == 200
    print(response.json())
    # response_2 = requests.get(f'{base_url}/')
    # assert response_2.json()['additionalneeds'] == 'Dinner'


def test_delete_booking(get_token, get_booking_id):
    token = {"Cookie": f"token = {get_token}"}
    response = requests.delete(f'{base_url}/{get_booking_id}', headers= token)
    assert response.status_code == 201

    response_2 = requests.get(f'{base_url}/{get_booking_id}')
    assert response_2.status_code == 404

def test_change_last_name(get_token, get_booking_id):
    payload = {
        "lastname": "Test_patch"
    }
    token = {"Cookie": f"token = {get_token}"}
    response = requests.patch(f'{base_url}/{get_booking_id}', headers=token, json = payload)
    assert response.json()['lastname'] == "Test_patch"
    print(response.json()['lastname'])



