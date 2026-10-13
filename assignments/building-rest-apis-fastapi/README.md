# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API with FastAPI that exposes data through HTTP endpoints and uses request validation and response models to manage a simple resource.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a FastAPI application that runs locally and serves a simple collection of data through API endpoints.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Define a basic route that returns a JSON response
- Start the app locally using a development server command
- Confirm the API responds successfully in a browser or API client

### 🛠️ Build CRUD Endpoints

#### Description
Add routes to read, create, and manage items in your API so clients can interact with the resource using standard HTTP methods.

#### Requirements
Completed program should:

- Create at least one `GET` route to return all items
- Create a `GET` route for a single item by identifier
- Add a `POST` route to create a new item
- Return JSON data in a clean and consistent format

### 🛠️ Add Validation and Error Handling

#### Description
Use request models and validation to make the API safer and easier to use for clients.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource data
- Validate incoming request data before saving it
- Return a useful error when a requested item does not exist
- Use clear field names and consistent response structure
