#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <form action="/echo_user_input" method="POST">
        <h2>Enter your exercise data:</h2>
        <div>
            <label for="exercise">Exercise:</label>
            <input type="text" id="exercise" name="exercise">
        </div>
        <div>
            <label for="weight">Weight (lbs):</label>
            <input type="number" id="weight" name="weight" step="0.01">
        </div>
        <div>
            <label for="reps">Reps:</label>
            <input type="number" id="reps" name="reps">
        </div>
        <input type="submit" value="Submit!">
    </form>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    exercise = request.form.get("exercise", "")
    weight = request.form.get("weight", "")
    reps = request.form.get("reps", "")
    return f"You entered: Exercise: {exercise}, Weight: {weight} lbs, Reps: {reps}"

if __name__ == "__main__":
    app.run(debug=True)
