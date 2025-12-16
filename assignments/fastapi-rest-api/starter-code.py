"""
Task Management API - Starter Code
FastAPI REST API for managing tasks

TODO: Complete the implementation by:
1. Creating the Task model
2. Implementing CRUD endpoints
3. Adding data persistence
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task Management API", version="1.0.0")

# TODO: Define your Task model here
# class Task(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False

# In-memory storage (replace with persistent storage later)
tasks = []


@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Task Management API"}


# TODO: Implement GET /tasks endpoint to retrieve all tasks


# TODO: Implement GET /tasks/{task_id} endpoint to retrieve a single task


# TODO: Implement POST /tasks endpoint to create a new task


# TODO: Implement PUT /tasks/{task_id} endpoint to update a task


# TODO: Implement DELETE /tasks/{task_id} endpoint to delete a task


# Run the app with: uvicorn starter-code:app --reload
