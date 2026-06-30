# CodeCraftHub

## Project Overview and Description

CodeCraftHub is a simple personalized learning platform designed for developers who want to track the courses they want to learn. This project is a great way to learn about REST APIs using Python and the Flask framework. The application allows you to perform CRUD (Create, Read, Update, Delete) operations on courses without the need for a database. All course data is stored in a simple JSON file.

## Features List

- **Track Courses**: Add, view, update, and delete courses you want to learn.
- **REST API**: Interact with the application using RESTful API endpoints.
- **JSON File Storage**: Course data is stored in a JSON file, making it easy to manage without a database.
- **Beginner-Friendly**: Designed to help beginners understand REST APIs and Flask.

## Installation Instructions

### Step-by-Step Guide

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/CodeCraftHub.git
   cd CodeCraftHub
   ```

3. **Create a Virtual Environment**: It's recommended to create a virtual environment for the project.
   ```bash
   python -m venv venv
   ```
   `venv` is a virtual environment that isolates project dependencies from your system Python.

4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**: Install required dependencies with pip.
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**:
   ```bash
   python app.py
   ```
   The application should start at `http://localhost:5000`.

7. **Explore the API**: Use the endpoint examples below with curl or Postman.

8. **Congratulations!** You've successfully installed and run CodeCraftHub.

## API Endpoints Documentation

### POST `/api/courses` - Add a New Course

**Request Body Example**

```json
{
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started"
}
```

**curl Command**

```bash
curl -X POST http://127.0.0.1:5000/api/courses \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Python Programming",
           "description": "Learn Python from scratch",
           "target_date": "2023-12-31",
           "status": "Not Started"
         }'
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started",
  "created_at": "2023-10-01 12:34:56"
}
```

### GET `/api/courses` - Get All Courses

**curl Command**

```bash
curl http://127.0.0.1:5000/api/courses
```

**Expected Response**

```json
[
  {
    "id": 1,
    "name": "Python Programming",
    "description": "Learn Python from scratch",
    "target_date": "2023-12-31",
    "status": "Not Started",
    "created_at": "2023-10-01 12:34:56"
  }
]
```

### GET `/api/courses/int:course_id` - Get a Specific Course

**curl Command**

```bash
curl http://127.0.0.1:5000/api/courses/1
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started",
  "created_at": "2023-10-01 12:34:56"
}
```

### PUT `/api/courses/int:course_id` - Update a Course

**Request Body Example**

```json
{
  "name": "Advanced Python Programming",
  "description": "Learn advanced Python concepts",
  "target_date": "2024-12-31",
  "status": "In Progress"
}
```

**curl Command**

```bash
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Advanced Python Programming",
           "description": "Learn advanced Python concepts",
           "target_date": "2024-12-31",
           "status": "In Progress"
         }'
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Advanced Python Programming",
  "description": "Learn advanced Python concepts",
  "target_date": "2024-12-31",
  "status": "In Progress",
  "created_at": "2023-10-01 12:34:56"
}
```

### DELETE `/api/courses/int:course_id` - Delete a Course

**curl Command**

```bash
curl -X DELETE http://127.0.0.1:5000/api/courses/1
```

**Expected Response**

```text
(Empty Response with Status Code 204)
```

## Testing Instructions

To test the API endpoints, you can use tools like Postman or curl. Below are some test cases for each endpoint.

### POST `/api/courses`

#### Test Case 1: Successful Operation

**Payload**

```json
{
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started"
}
```

**Command**

```bash
curl -X POST http://127.0.0.1:5000/api/courses \
     -H "Content-Type: application/json" \
     -d '{"name": "Python Programming", "description": "Learn Python from scratch", "target_date": "2023-12-31", "status": "Not Started"}'
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started",
  "created_at": "2023-10-01 12:34:56"
}
```

#### Test Case 2: Missing Fields

**Payload**

```json
{
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "status": "Not Started"
}
```

**Command**

```bash
curl -X POST http://127.0.0.1:5000/api/courses \
     -H "Content-Type: application/json" \
     -d '{"name": "Python Programming", "description": "Learn Python from scratch", "status": "Not Started"}'
```

**Expected Response**

```json
{
  "error": "Missing required field: target_date"
}
```

### GET `/api/courses`

#### Test Case 1: Successful Operation

**Command**

```bash
curl http://127.0.0.1:5000/api/courses
```

**Expected Response**

```json
[
  {
    "id": 1,
    "name": "Python Programming",
    "description": "Learn Python from scratch",
    "target_date": "2023-12-31",
    "status": "Not Started",
    "created_at": "2023-10-01 12:34:56"
  }
]
```

### GET `/api/courses/int:course_id`

#### Test Case 1: Successful Operation

**Command**

```bash
curl http://127.0.0.1:5000/api/courses/1
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Python Programming",
  "description": "Learn Python from scratch",
  "target_date": "2023-12-31",
  "status": "Not Started",
  "created_at": "2023-10-01 12:34:56"
}
```

#### Test Case 2: Course Not Found

**Command**

```bash
curl http://127.0.0.1:5000/api/courses/999
```

**Expected Response**

```json
{
  "error": "Course not found"
}
```

### PUT `/api/courses/int:course_id`

#### Test Case 1: Successful Operation

**Payload**

```json
{
  "name": "Advanced Python Programming",
  "description": "Learn advanced Python concepts",
  "target_date": "2024-12-31",
  "status": "In Progress"
}
```

**Command**

```bash
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Advanced Python Programming", "description": "Learn advanced Python concepts", "target_date": "2024-12-31", "status": "In Progress"}'
```

**Expected Response**

```json
{
  "id": 1,
  "name": "Advanced Python Programming",
  "description": "Learn advanced Python concepts",
  "target_date": "2024-12-31",
  "status": "In Progress",
  "created_at": "2023-10-01 12:34:56"
}
```

#### Test Case 2: Course Not Found

**Command**

```bash
curl -X PUT http://127.0.0.1:5000/api/courses/999 \
     -H "Content-Type: application/json" \
     -d '{"name": "Advanced Python Programming", "description": "Learn advanced Python concepts", "target_date": "2024-12-31", "status": "In Progress"}'
```

**Expected Response**

```json
{
  "error": "Course not found"
}
```

### DELETE `/api/courses/int:course_id`

#### Test Case 1: Successful Operation

**Command**

```bash
curl -X DELETE http://127.0.0.1:5000/api/courses/1
```

**Expected Response**

```text
(Empty Response with Status Code 204)
```

#### Test Case 2: Course Not Found

**Command**

```bash
curl -X DELETE http://127.0.0.1:5000/api/courses/999
```

**Expected Response**

```json
{
  "error": "Course not found"
}
```

## Troubleshooting Common Issues

- **Python Not Installed**: Ensure Python is installed by running `python --version` in your terminal. If not installed, download it from [python.org](https://www.python.org/).
- **Dependencies Not Found**: Run `pip install -r requirements.txt` to install all required packages.
- **Flask Application Not Running**: Make sure you are in the correct directory and run `python app.py` to start the Flask application.
- **JSON File Not Found**: If `courses.json` is missing, the application will create it automatically when you run it for the first time.

## Project Structure Explanation

```text
CodeCraftHub/
|
|-- app.py           # Main Flask application
|-- courses.json     # JSON file to store course data
`-- requirements.txt # Python dependencies
```

- `app.py`: This file contains the main Flask application code, including all the REST API endpoints.
- `courses.json`: This file stores the course data. It is created automatically if it does not exist.
- `requirements.txt`: This file lists the Python dependencies needed for the project.

## Conclusion

CodeCraftHub is a simple yet effective way to learn about REST APIs using Python and Flask. By following this README, you should be able to set up, run, and test the application easily. If you have any questions or run into issues, feel free to reach out. Happy coding!
