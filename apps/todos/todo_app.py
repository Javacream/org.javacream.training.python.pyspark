from todo_services import read_todos, calculate_open_todos, write_result

def main():
    print('start main')
    todo_file_path = 'data/todos.txt'
    todos = read_todos(todo_file_path) # implizit: path = todo_file_path
    open_todos = calculate_open_todos(todos)
    write_result(open_todos)
    print('finish main')

if __name__ == '__main__': # Typisches Muster für Python-Anwendungen
    main()    