from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Define the path to the JSON file
COURSES_FILE = 'courses.json'


# Helper function to load courses from JSON file
def load_courses():
    """
    Load courses from the JSON file.
    If the file doesn't exist, create it with an empty list.
    """
    if not os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, 'w') as file:
            json.dump([], file)

    try:
        with open(COURSES_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Handle file read errors
        return []


# Helper function to save courses to JSON file
def save_courses(courses):
    """
    Save the list of courses to the JSON file.
    """
    try:
        with open(COURSES_FILE, 'w') as file:
            json.dump(courses, file, indent=4)
    except IOError:
        # Handle file write errors
        print("Error writing to the file.")


# POST /api/courses - Add a new course
@app.route('/api/courses', methods=['POST'])
def add_course():
    """
    Add a new course to the list.
    """
    courses = load_courses()
    data = request.get_json()

    # Validate required fields
    required_fields = ['name', 'description', 'target_date', 'status']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Validate status
    valid_statuses = ["Not Started", "In Progress", "Completed"]
    if data['status'] not in valid_statuses:
        return jsonify({'error': f'Invalid status value: {data["status"]}'}), 400

    # Generate course ID
    new_id = len(courses) + 1

    # Generate timestamp for created_at
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create new course
    new_course = {
        'id': new_id,
        'name': data['name'],
        'description': data['description'],
        'target_date': data['target_date'],
        'status': data['status'],
        'created_at': created_at
    }

    courses.append(new_course)
    save_courses(courses)

    return jsonify(new_course), 201


# GET /api/courses - Get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Get all courses from the list.
    """
    courses = load_courses()
    return jsonify(courses)


# GET /api/courses/<int:course_id> - Get a specific course
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Get a specific course by its ID.
    """
    courses = load_courses()
    course = next((course for course in courses if course['id'] == course_id), None)

    if course:
        return jsonify(course)
    else:
        return jsonify({'error': 'Course not found'}), 404


# PUT /api/courses/<int:course_id> - Update a course
@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update an existing course.
    """
    courses = load_courses()
    course = next((course for course in courses if course['id'] == course_id), None)

    if course:
        data = request.get_json()

        # Validate required fields for update
        required_fields = ['name', 'description', 'target_date', 'status']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Validate status
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if data['status'] not in valid_statuses:
            return jsonify({'error': f'Invalid status value: {data["status"]}'}), 400

        # Update course data
        course.update({
            'name': data['name'],
            'description': data['description'],
            'target_date': data['target_date'],
            'status': data['status'],
            'created_at': course['created_at']  # Keep the original created_at timestamp
        })

        save_courses(courses)
        return jsonify(course)
    else:
        return jsonify({'error': 'Course not found'}), 404


# DELETE /api/courses/<int:course_id> - Delete a course
@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete a course by its ID.
    """
    courses = load_courses()
    course = next((course for course in courses if course['id'] == course_id), None)

    if course:
        courses.remove(course)
        save_courses(courses)
        return '', 204
    else:
        return jsonify({'error': 'Course not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)