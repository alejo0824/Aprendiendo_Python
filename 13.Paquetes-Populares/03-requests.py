
import requests

url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url, timeout=10)
# print(
#     r.status_code,
#     r.text
# )

r = r.json()

for user in r:
    print(user["name"])

url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=10)
print(r.json())

# ======================= POST =======================
url = "https://jsonplaceholder.typicode.com/users/"
user = {
    "id": 11,
    "name": "Chanchito Feliz"
}

r = requests.post(url, timeout=10, data=user)
print(r.status_code)


# ======================= PUT =======================
url2 = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Chanchito Feliz"
}

r = requests.put(url2, timeout=10, data=user)
print(r.status_code)

# ======================= DELETE =======================
url = "https://jsonplaceholder.typicode.com/users/3"
user = {
    "name": "Chanchito Feliz"
}

r = requests.delete(url, timeout=10, data=user)
print(r.status_code)

# ======================= Headers =======================
url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "456357"
headers = {
    "Authorization": f"Bearer {apikey}"
}
