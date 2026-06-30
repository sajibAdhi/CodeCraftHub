from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# Load courses data from JSON file
with open('courses.json') as file:
    courses = json.load(file)

# Retrieve all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

# Add a new course
@app.route('/courses', methods=['POST'])
def add_course():
    new_course = request.json
    courses.append(new_course)
    save_courses()
    return jsonify(new_course), 201

# Retrieve a specific course
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    if 0 <= course_id < len(courses):
        return jsonify(courses[course_id])
    return jsonify({'error': 'Course not found'}), 404

# Update a specific course
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    if 0 <= course_id < len(courses):
        updated_course = request.json
        courses[course_id] = updated_course
        save_courses()
        return jsonify(updated_course)
    return jsonify({'error': 'Course not found'}), 404

# Delete a specific course
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    if 0 <= course_id < len(courses):
        deleted_course = courses.pop(course_id)
        save_courses()
        return jsonify(deleted_course)
    return jsonify({'error': 'Course not found'}), 404

# Save courses data to JSON file
def save_courses():
    with open('courses.json', 'w') as file:
        json.dump(courses, file)

# Render course details page
@app.route('/courses/<int:course_id>/details')
def course_details(course_id):
    if 0 <= course_id < len(courses):
        return render_template('course.html', course=courses[course_id])
    return redirect(url_for('index'))

# Render index page
@app.route('/')
def index():
    return render_template('index.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)