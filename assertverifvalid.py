import requests
def main():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/84 ")
    print(response_body)
    print(response_body.json())

    data = response_body.json()
    print(type(data))

#assertions - verfication of keys
    assert 'firstname' in data, "incorrect first name"
    assert 'lastname' in data, "incorrect last name"

#assertions - verification of data
    assert data["firstname"] == "Josh", "Incorrect firstname"
    assert data["lastname"] == "Allen", "incorrect last name"
    assert data ["bookingdates"]["checkin"] == "2018-01-01", "Incorrect message"
if __name__ == '__main__':
    main()
