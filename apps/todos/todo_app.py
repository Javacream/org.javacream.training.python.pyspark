def read_todos(path):
    return []
def calculate_open_todos(todos):
    return []
def write_result(result):
    pass

def main():
    print('start main')
    todo_file_path = ''
    todos = read_todos(todo_file_path) # implizit: path = todo_file_path
    open_todos = calculate_open_todos(todos)
    write_result(open_todos)
    print('finish main')

if __name__ == '__main__': # Typisches Muster für Python-Anwendungen
    main()    