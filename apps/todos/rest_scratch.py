import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = response.text
todos_dict = json.loads(todos)
print(todos)
