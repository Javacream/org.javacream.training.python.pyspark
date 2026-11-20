import json

def read_todos(path):
    with open(path, 'rt', encoding='utf-8') as todos_file:
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
    return todos
def calculate_open_todos(todos):
    open_todos = [todo for todo in todos if todo["status"] == False]
    return open_todos
def calculate_finished_todos(todos):
    open_todos = [todo for todo in todos if todo["status"] == True]
    return open_todos
def write_result(result):
 with open('data/open_todos.json', "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)
 with open('data/open_todos.data', "w", encoding="utf-8") as file:
        file.write(str(result))