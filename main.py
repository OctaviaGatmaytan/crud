from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy groceries", "done": True},
    {"id": 2, "title": "Work on assignments", "done": False},
    {"id": 3, "title": "Visit grandma", "done": False},
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_tasks(id:int):
    for task in tasks:
        if task["id"] == id:
            return task   
        raise HTTPException(status_code=404, detail=f"Task {id} not found")