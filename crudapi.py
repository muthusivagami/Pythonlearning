import requests
def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/972")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code==200:
        print("get requet successfull")
    else:
        print("get request is not successfull")

if __name__ == "__main__":
    main()