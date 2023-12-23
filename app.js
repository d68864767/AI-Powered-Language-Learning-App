```javascript
document.addEventListener('DOMContentLoaded', function() {
    const exerciseForm = document.querySelector('#exercise-form');
    const progressButton = document.querySelector('#progress-button');
    const communityButton = document.querySelector('#community-button');

    exerciseForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const user_input = document.querySelector('#user-input').value;
        const exercise_type = document.querySelector('#exercise-type').value;

        fetch('/exercise', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_input: user_input,
                exercise_type: exercise_type,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Display the result of the exercise
            const resultElement = document.querySelector('#result');
            resultElement.textContent = data.result;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    progressButton.addEventListener('click', function(event) {
        event.preventDefault();

        fetch('/progress')
        .then(response => response.json())
        .then(data => {
            // Display the user's progress
            const progressElement = document.querySelector('#progress');
            progressElement.textContent = JSON.stringify(data.progress);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    communityButton.addEventListener('click', function(event) {
        event.preventDefault();

        fetch('/community')
        .then(response => response.json())
        .then(data => {
            // Display the community posts
            const communityElement = document.querySelector('#community');
            communityElement.textContent = JSON.stringify(data.posts);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
```
