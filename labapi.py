import requests
#requests are needed to make a different http methods
response_body=requests.get("https://restful-booker.herokuapp.com/booking/1000")
print(response_body.text)
print(response_body.status_code)
print(response_body.json())