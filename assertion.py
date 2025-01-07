import requests
def main():
 response_body=requests.get("https://restful-booker.herokuapp.com/booking/84")
 assert response_body.status_code == 200

id = 90
url = "https://restful-booker.herokuapp.com/booking/"
fullurl = url + str(id)
print (fullurl)
response_body1= requests.get(fullurl)
assert response_body1.status_code == 200

if __name__ == '__main__':
    main()