#!/usr/bin/env python3

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Define a simple HTML form with fields for multiple inputs.
html_form = """
<form action="/submit" method="post">
    {% for i in range(rows) %}
    <div>
        <label for="exercise{{i}}">Exercise:</label>
        <input type="text" name="exercise{{i}}" required>
        
        <label for="weight{{i}}">Weight:</label>
        <input type="number" name="weight{{i}}" step="0.1" required>
        
        <label for="reps{{i}}">Reps:</label>
        <input type="number" name="reps{{i}}" required>
    </div>
    {% endfor %}
    <input type="submit">
</form>
"""

@app.route('/', methods=['GET'])
def main():
    # Render the form with 5 rows (or any other number you want)
    return render_template_string(html_form, rows=5)

@app.route('/submit', methods=['POST'])
def submit():
    # Extract the data for each exercise entry
    exercises = []
    for i in range(5):  # Assuming 5 rows as before
        exercise = request.form.get(f'exercise{i}')
        weight = request.form.get(f'weight{i}')
        reps = request.form.get(f'reps{i}')
        exercises.append(f'Exercise: {exercise}, Weight: {weight}, Reps: {reps}')
    # Combine the data into a response
    return '<br>'.join(exercises)

if __name__ == '__main__':
    app.run(debug=True)
