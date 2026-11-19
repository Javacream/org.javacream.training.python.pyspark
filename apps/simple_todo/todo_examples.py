with open('data/todos.txt', 'rt', encoding='utf-8') as todos_file:
    raw_line = todos_file.read()

lines = raw_line.split('\n')
todos = list()
for line in lines:
    if line.strip() != "":
        description, priority, status = line.split(',')
        priority = int(priority)
        status = bool(int(status))
        todo = {'description': description, 'priority': priority, 'status': status}
        todos.append(todo)

open_todos = [todo for todo in todos if todo["status"] == False]

closed_todos = [todo for todo in todos if todo["status"]]

high_priority_todos = [todo for todo in todos if todo["priority"] > 5]

low_priority_todos = [todo for todo in todos if todo["priority"] <= 5]

open_todos_descriptions = [todo['description'] for todo in todos if todo["status"] == True]

todos_with_description_starting_with_D = [todo for todo in todos if todo["description"].startswith('D')]

print('Done')
