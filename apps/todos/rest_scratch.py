import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = response.json()
print(todos)
