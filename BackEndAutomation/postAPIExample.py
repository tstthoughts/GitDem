import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

add_url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(add_url,json=addBookPayload("fewfrewre"),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

del_url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers = {"Content-Type": "application/json"}
bookId = response_json['ID']
print(bookId)
# Delete Book -
response_deleteBook = requests.post(del_url, json={

    "ID": bookId
}, headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

#Authentication  ::: requests can also ignore verifying the SSL certificate if you set verify to False.
url = "https://api.github.com/user"
github_response = requests.get(url,verify=False,auth=('rahulshettcademy',getPassword()))

print(github_response.status_code)

