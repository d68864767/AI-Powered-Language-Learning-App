```python
from flask import Flask, render_template, request
import ai_model
import speech_recognition
import progress_tracker
import community_features

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercise', methods=['POST'])
def exercise():
    user_input = request.form['user_input']
    exercise_type = request.form['exercise_type']
    
    if exercise_type == 'pronunciation':
        result = speech_recognition.check_pronunciation(user_input)
    else:
        result = ai_model.check_answer(user_input, exercise_type)
    
    return render_template('exercise.html', result=result)

@app.route('/progress')
def progress():
    user_progress = progress_tracker.get_progress()
    return render_template('progress.html', progress=user_progress)

@app.route('/community')
def community():
    community_posts = community_features.get_posts()
    return render_template('community.html', posts=community_posts)

if __name__ == '__main__':
    app.run(debug=True)
```
