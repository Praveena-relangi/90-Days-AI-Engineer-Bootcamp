import requests 

# example for get() call of REST API
choose_api_call = input("which api call you want to make? : ").lower()
if choose_api_call == "get":
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response) # returns response object
    print(response.status_code) # returns status code of response
    print(response.text) # returns string of output
    print(response.json()) # returns python dict
    data = response.json()
    print(type(data)) # dict
    print(data['title'])
elif choose_api_call == "post":
    data = {
        "title": "Praveena Learning REST API",
        "body": "This is my first POST request.",
        "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json= data)
    print(response.status_code)
    print(response.json())
elif choose_api_call == "put":
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                            json = {
                                "title" : "Updated Title",
                                "body" : "Updated Body",
                                "userId" : 1
                            })
    print(response.status_code)
    print(response.json())
elif choose_api_call == "delete":
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(response.status_code)
    print(response.text)
else:
    print("choose the correct call!!!")
