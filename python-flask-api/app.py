import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS
DATABASE = 'leacreer_db.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

# Retrieve all question groups
@app.route('/question_groups', methods=['GET'])
def get_question_groups():
    conn = get_db_connection()
    groups = conn.execute('SELECT * FROM QUESTION_GROUP').fetchall()
    conn.close()
    return jsonify([dict(row) for row in groups])

# Retrieve a single question group by ID
@app.route('/question_groups/<int:group_id>', methods=['GET'])
def get_question_group_by_id(group_id):
    conn = get_db_connection()
    group = conn.execute('SELECT * FROM QUESTION_GROUP WHERE GROUP_ID = ?', 
                         (group_id,)).fetchone()
    conn.close()
    if group is None:
        return "Question group not found for the given ID", 404
    return jsonify(dict(group))

# Retrieve all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM QUESTION').fetchall()
    conn.close()
    return jsonify([dict(row) for row in questions])

# Retrieve a single question by ID
@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):
    conn = get_db_connection()
    question = conn.execute('SELECT * FROM QUESTION WHERE QUESTION_ID = ?', 
                            (question_id,)).fetchone()
    conn.close()
    if question is None:
        return "Question not found for the given ID", 404
    return jsonify(dict(question))

# Retrieve all submissions
@app.route('/submissions', methods=['GET'])
def get_submissions():
    conn = get_db_connection()
    submissions = conn.execute('SELECT * FROM SUBMISSION').fetchall()
    conn.close()
    return jsonify([dict(row) for row in submissions])

# Retrieve submission responses for a given submission ID
@app.route('/submissions/<submission_id>/responses', methods=['GET'])
def get_submission_responses(submission_id):
    conn = get_db_connection()
    responses = conn.execute('SELECT * FROM SUBMISSION_RESPONSE WHERE SUBMISSION_ID = ?', 
                             (submission_id,)).fetchall()
    conn.close()
    if responses is None:
        return "Responses not found for the given submission ID", 404
    return jsonify([dict(row) for row in responses])

if __name__ == '__main__':
    app.run(debug=True)


# Retrieve all questions where 'FitmentQuestion' is 'Yes'
@app.route('/fitment_questions', methods=['GET'])
def get_questions_fitment_yes():
    conn = get_db_connection()
    questions = conn.execute('SELECT Question FROM mission_capability WHERE FitmentQuestion = "Yes"').fetchall()
    conn.close()
    return jsonify([row['Question'] for row in questions])

# Retrieve a parent question
@app.route('/questions/parent/<int:parent_id>', methods=['GET'])
def get_parent_question(parent_id):
    conn = get_db_connection()
    # Fetch child questions linked to the specified parent ID
    parent_question = conn.execute('SELECT Question FROM mission_capability WHERE ParentID = ?', (parent_id,)).fetchone()
    conn.close()

    if not parent_question:
        return "No parent question found for the given parent ID", 404

    return jsonify(parent_question['Question'])

# Retrieve a parent question's ParentID
@app.route('/questions/parent_id/<string:parent_text>', methods=['GET'])
def get_parent_id(parent_text):
    conn = get_db_connection()
    # Fetch the ParentID for the given parent question text
    parent_question = conn.execute('SELECT ParentID FROM mission_capability WHERE Question = ? AND FitmentQuestion = "Yes"', (parent_text,)).fetchone()
    conn.close()

    # Check if a parent question was found and if it has a ParentID
    if not parent_question or parent_question['ParentID'] is None:
        return "No parent question found for the given parent text, or no ParentID associated with the found question", 404

    return jsonify(parent_question['ParentID'])

# Retrieve all subquestions from a parent question
@app.route('/questions/children/<int:parent_id>', methods=['GET'])
def get_child_questions(parent_id):
    conn = get_db_connection()
    # Fetch child questions linked to the specified parent ID
    child_questions = conn.execute('SELECT * FROM mission_capability WHERE LinkedParentID = ?', (parent_id,)).fetchall()
    conn.close()

    if not child_questions:
        return "No child questions found for the given parent ID", 404

    return jsonify([dict(question) for question in child_questions])

@app.route('/mission_capabilities', methods=['POST'])
def create_mission_capability():
    new_mission = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO mission_capability (Subsystem, MissionEssentialFunction, TestItemDescriptor, Question, Vehicle, FitmentQuestion, GoodDescriptor, BadDescriptor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (new_mission['Subsystem'], new_mission['MissionEssentialFunction'], new_mission['TestItemDescriptor'], new_mission['Question'], new_mission['Vehicle'], new_mission['FitmentQuestion'], new_mission['GoodDescriptor'], new_mission['BadDescriptor']))
    conn.commit()
    conn.close()
    return jsonify(new_mission), 201

@app.route('/mission_capabilities/<int:id>', methods=['PUT'])
def update_mission_capability(id):
    update_mission = request.json
    conn = get_db_connection()
    conn.execute('UPDATE mission_capability SET Subsystem = ?, MissionEssentialFunction = ?, TestItemDescriptor = ?, Question = ?, Vehicle = ?, FitmentQuestion = ?, GoodDescriptor = ?, BadDescriptor = ? WHERE id = ?',
                 (update_mission['Subsystem'], update_mission['MissionEssentialFunction'], update_mission['TestItemDescriptor'], update_mission['Question'], update_mission['Vehicle'], update_mission['FitmentQuestion'], update_mission['GoodDescriptor'], update_mission['BadDescriptor'], id))
    conn.commit()
    conn.close()
    return jsonify(update_mission)

@app.route('/mission_capabilities/<int:id>', methods=['DELETE'])
def delete_mission_capability(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM mission_capability WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return "Mission capability deleted", 200

if __name__ == '__main__':
     app.run(host='localhost', port=8000)