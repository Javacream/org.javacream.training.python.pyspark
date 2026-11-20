# from todo_services import read_todos, calculate_open_todos, write_result
import todo_services

def main():
    print('start main')
    todo_file_path = 'data/todos.txt'
    todos = todo_services.read_todos(todo_file_path) # implizit: path = todo_file_path
    open_todos = todo_services.calculate_open_todos(todos)
    todo_services.write_result(open_todos)
    print('finish main')

if __name__ == '__main__': # Typisches Muster für Python-Anwendungen
    main()    