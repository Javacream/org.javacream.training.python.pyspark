todos = [
    {'description': 'Eat', "priority": 5, 'status': False},
    {'description': 'Sleep', "priority": 2, 'status': True},
    {'description': 'Drink', "priority": 9, 'status': False},
    {'description': 'Walk', "priority": 9, 'status': False},
    {'description': 'Talk', "priority": 3, 'status': True}
]

open_todos = []
for todo in todos:
    if todo["status"] == False:
        open_todos.append(todo)

closed_todos = []
for todo in todos:
    if todo["status"] == True:
        closed_todos.append(todo)

high_priority_todos = []
for todo in todos:
    if todo["priority"] > 5:
        high_priority_todos.append(todo)

low_priority_todos = []
for todo in todos:
    if todo["priority"] <= 5:
        low_priority_todos.append(todo)

open_todos_descriptions = []
for todo in todos:
    if todo["status"] == True:
        open_todos_descriptions.append(todo['description'])

todos_with_description_starting_with_D = []
for todo in todos:
    if todo["description"].startswith('D'):
        todos_with_description_starting_with_D.append(todo)

print('Done')
