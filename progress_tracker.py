```python
class ProgressTracker:
    def __init__(self):
        self.progress = {}

    def update_progress(self, user_id, exercise_type, result):
        if user_id not in self.progress:
            self.progress[user_id] = {}

        if exercise_type not in self.progress[user_id]:
            self.progress[user_id][exercise_type] = {'correct': 0, 'total': 0}

        self.progress[user_id][exercise_type]['total'] += 1

        if result:
            self.progress[user_id][exercise_type]['correct'] += 1

    def get_progress(self, user_id):
        if user_id in self.progress:
            return self.progress[user_id]
        else:
            return None

progress_tracker = ProgressTracker()

def update_progress(user_id, exercise_type, result):
    progress_tracker.update_progress(user_id, exercise_type, result)

def get_progress(user_id):
    return progress_tracker.get_progress(user_id)
```
