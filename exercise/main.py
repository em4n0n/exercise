from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    age = int(request.form['age'])
    gender = request.form['gender']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    goal = request.form['goal']
    experience = request.form['experience']
    time = int(request.form['time'])

    plan = create_plan(age, gender, height, weight, goal, experience, time)

    return render_template_string(f"""
        <h2>Your Workout Plan</h2>
        <pre>{plan}</pre>
        <a href="/">Back</a>
    """)

def create_plan(age, gender, height, weight, goal, experience, time):
    if goal == 'Lose Fat':
        return f"""\
3 Days HIIT (30 mins)
2 Days Strength Training
2 Days Rest or Light Cardio

Focus: Calorie Deficit, Full-body workouts, 8–12 reps per set."""
    
    elif goal == 'Build Muscle':
        return f"""\
4 Days Strength Training (Push/Pull/Legs Split)
1 Day HIIT or Conditioning
2 Days Rest

Focus: Progressive Overload, Protein Intake, 6–10 reps."""
    
    else:  # Maintain
        return f"""\
3 Days Strength Training
2 Days Cardio
2 Days Active Rest

Focus: Balanced routine, Moderate intensity, 10–12 reps."""

if __name__ == '__main__':
    app.run(debug=True)
