todos = [
    {'description': 'Eat', "priority": 5, 'status': False},
    {'description': 'Sleep', "priority": 2, 'status': True},
    {'description': 'Drink', "priority": 9, 'status': False},
    {'description': 'Walk', "priority": 9, 'status': False},
    {'description': 'Talk', "priority": 3, 'status': True}
]

# Python Comprehensions, eine Art integrierte Selektionssprache
open_todos = [todo for todo in todos if todo["status"] == False]

closed_todos = [todo for todo in todos if todo["status"]]

high_priority_todos = [todo for todo in todos if todo["priority"] > 5]

low_priority_todos = [todo for todo in todos if todo["priority"] <= 5]

open_todos_descriptions = [todo['description'] for todo in todos if todo["status"] == True]

todos_with_description_starting_with_D = [todo for todo in todos if todo["description"].startswith('D')]

print('Done')
