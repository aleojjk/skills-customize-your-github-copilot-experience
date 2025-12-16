# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to manage a collection of resources. This assignment will help you practice API design, HTTP methods, request validation, and working with modern Python web frameworks.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API for managing tasks using FastAPI. The API should support creating, reading, updating, and deleting tasks (CRUD operations). Each task should have an ID, title, description, and completion status.

#### Requirements
Completed program should:

- Define a Task model with fields: id, title, description, and completed status
- Implement GET endpoint to retrieve all tasks
- Implement GET endpoint to retrieve a single task by ID
- Implement POST endpoint to create a new task
- Implement PUT endpoint to update an existing task
- Implement DELETE endpoint to remove a task
- Include proper HTTP status codes (200, 201, 404, etc.)
- Use FastAPI's automatic request validation
- Include API documentation using FastAPI's built-in Swagger UI


### 🛠️ Add Data Persistence

#### Description
Extend your API to store tasks persistently using a JSON file or SQLite database instead of in-memory storage.

#### Requirements
Completed program should:

- Store tasks in a JSON file or SQLite database
- Load existing tasks when the API starts
- Save tasks automatically when they are created, updated, or deleted
- Handle file/database errors gracefully
- Ensure data persists between API restarts
