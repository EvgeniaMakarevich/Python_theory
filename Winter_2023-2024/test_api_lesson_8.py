import pytest
import requests

# from my_module import sum_it
#
# def test_1():
#     assert sum_it(4,8) == 12, 'Wrong result'
#
# def test_2():
#     assert sum_it(5,12) == 15, 'Wrong result'

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
STATUS_OK = 200
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'

@pytest.fixture(scope='function')
def booking_id():
    payload = {
        "firstname": "John",
        "lastname": "Test",
        "totalprice": 333,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-03-12",
            "checkout": "2023-10-12"
        },
        "additionalneeds": "Lunch"}
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_get_all_bookings():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    # print(f'\n{len(response.json())}')
    # assert len(response.json()) == 1765, 'Wrong number'
    # print(response.headers)
    assert 'Connection' in response.headers, 'Theres no such key'

def test_get_booking_withid():
    response = requests.get(f'{BASE_URL}/1')
    response.data = response.json()
    expected_key = ['firstname','lastname','totalprice','depositpaid','bookingdates']
    assert response.data['firstname'] == 'Eric'
    assert response.status_code == STATUS_OK
    for key in expected_key:
        assert key in response.data.keys()


def test_create_booking():
    payload = {
    "firstname": "Evgenia",
    "lastname": "Test",
    "totalprice": 333,
    "depositpaid":True,
    "bookingdates": {
        "checkin": "2023-03-12",
        "checkout": "2023-10-12"
    },
    "additionalneeds": "Lunch"}
    response = requests.post(BASE_URL,json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK
    id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{id}')
    assert get_response.json()['firstname'] == 'Evgenia'


def test_check_created_booking_with_fixture(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.json()['firstname'] == 'John'


@pytest.fixture(scope='function')
def token():
    payload = {
    "username" : "admin",
    "password" : "password123"}
    response = requests.post(AUTH_URL, json=payload)
    token = response.json()['token']
    assert response.status_code == 200
    yield token

def test_delete_new_booking(booking_id,token):
    headers = {'Cookie': f'token = {token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    assert get_response.status_code == 404


def test_update_booking(booking_id,token):
    headers = {'Cookie': f'token={token}'}
    payload = {"firstname" : "test_put",
    "lastname" : "Brown",
    "totalprice" : 222,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-01-01",
        "checkout" : "2024-01-01"
    },
    "additionalneeds" : "Dinner"}
    response = requests.put(f'{BASE_URL}/{booking_id}', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()['firstname'] == 'test_put'
    assert response.json()['totalprice'] == 222
    print(response.json())


def test_patch_booking(booking_id,token):
    headers = {'Cookie': f'token={token}'}
    payload = {"firstname": "test_patch",
               "lastname": "Patch",
               "totalprice": 444,
               }
    response = requests.patch(f'{BASE_URL}/{booking_id}', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()['firstname'] == 'test_patch'
    assert response.json()['totalprice'] == 444
    assert response.json()['lastname'] == 'Patch'
    print(response.json())


