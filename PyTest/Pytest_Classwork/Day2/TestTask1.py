
import requests

# requests = requests.get("https://petstore.swagger.io/v2/store/inventory")
# requests = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")
#
# print(requests.status_code)
# print(requests.text)
# print(requests.json())

# expected = 200
# actual = request.status_code
# assert actual == expected, "Wrong response"
"""
payload =  {
        "id": 123321,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
request = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
print(request.text)
# expected = 200
# actual = requests.status_code
# assert expected == actual ,f"Not Equal  {actual}"

request = requests.get("https://petstore.swagger.io/v2/pet/123321")
print(request.text)
print(request.status_code)

##delete method
response = requests.delete("https://petstore.swagger.io/v2/pet/123321")
print(response.status_code)
"""
def Add_pet():
    body = {

        "id": 123,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doge",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post('https://petstore.swagger.io/v2/pet', json=body)
    assert response.status_code == 200
    print(response.status_code)
    # print(response.json()["id"] , "Pet Successfully registered")
    return response.json()['id']

def check_pet(p_id):
    resp = requests.get(f'https://petstore.swagger.io/v2/pet/{p_id}')
    print(resp.status_code)
    print(resp.json())
    act = resp.json()["id"]
    if(act == p_id):
        print("Pet is registered already")
    else:
        print("Pet not found")

def delete_pet(id):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{id}')
    print(response.status_code, "Pet Successfully delted")

id = Add_pet()
check_pet(id)
delete_pet(id)
