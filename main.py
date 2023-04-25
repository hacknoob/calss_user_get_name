import requests, json
url='https://jsonplaceholder.typicode.com/users'
req= requests.get(name)
data=json.loads(req.text)
for item in reversed(data):
    print (item)
    print(data[0]['name'])

class MyUser:
    def_init_(self, name, username, email):
    self.name=name
    self.email=email
    self.username=username

    def_str_(self):
    return f"{self.name}({self.username})({self.email})"
