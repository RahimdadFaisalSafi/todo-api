from fastapi import FastAPI

app = FastAPI()

todo_1 = {"id":1, "title": "Mein erstes Todo", "status": "open"}
todos = [todo_1]

@app.get('/')
def root():
    return 'Hello World'
@app.get('/todos')
def get_todos(): 
    return todos

@app.post("/todos")
def post_todos(item):
    print(item)
    todos.append(item)
    return todos