```python
class CommunityFeatures:
    def __init__(self):
        self.posts = []

    def add_post(self, user_id, post_content):
        post = {
            'user_id': user_id,
            'content': post_content
        }
        self.posts.append(post)

    def get_posts(self):
        return self.posts

community_features = CommunityFeatures()

def add_post(user_id, post_content):
    community_features.add_post(user_id, post_content)

def get_posts():
    return community_features.get_posts()
```
