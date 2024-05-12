from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

items = []

dummy_posts = [
    {"id": 1, "title": "Post 1", "summary": "Summary to post 1", "tags": ["tag1", "tag2"], "content": {"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris bibendum lectus nunc, vitae consequat ex molestie vel. Ut elementum iaculis tellus quis finibus. Phasellus tempus tincidunt lectus non maximus. Vestibulum lacinia nec nunc a finibus. Aenean at suscipit ex. Vivamus condimentum blandit velit ac vulputate. Aliquam ac faucibus est. Fusce molestie, enim ut laoreet vestibulum, nisi dui fermentum urna, vel sagittis elit velit non nunc.", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img1.jpg"}},
    {"id": 2, "title": "Post 2", "summary": "Donec sagittis sed neque vel elementum. Pellentesque convallis ligula ex, nec hendrerit dolor luctus a. Aenean in tincidunt velit. Nullam feugiat nisi eget luctus rhoncus. ","tags": ["tag2", "tag3"], "content": {"text": "Curabitur tincidunt elit metus, ac auctor nibh pretium id. Integer ornare ex risus, at sagittis sapien fermentum ut. Vivamus lacinia tincidunt ante, a convallis velit consectetur a. Integer ultrices nulla sit amet lorem gravida elementum. Ut mattis, lacus fringilla posuere fringilla, diam est egestas leo, quis posuere augue ligula sed quam. Aenean porta erat nec vehicula mollis. Mauris non arcu id nisl finibus tristique sit amet at risus. Nunc pulvinar augue ipsum, at venenatis erat suscipit ac. Maecenas laoreet lacinia facilisis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam placerat urna quam, ut ultrices elit iaculis sit amet.", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img2.jpg"}},
    {"id": 3, "title": "Post 3", "summary": "Summary to post 3 Summary to post 3","tags": ["tag4", "tag5"], "content": {"text": "Fusce vitae dictum eros, quis luctus ligula. Curabitur ullamcorper volutpat erat, in porta ex hendrerit ut. Proin varius at nisl vel tempus. Sed consequat odio ex, sit amet placerat dui ullamcorper vitae. ", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img3.jpg"}},
    {"id": 4, "title": "Post 4", "summary": "Summary to post 4 Summary to post 4 Summary to post 4","tags": ["tag1", "tag3"], "content": {"text": "Sample content for post 4.", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img4.jpg"}},
    {"id": 5, "title": "Post 5", "summary": "Summary to post 5 Summary to post 5","tags": ["tag5", "tag4"], "content": {"text": "Curabitur quis ipsum ornare, vulputate ante ac, egestas felis. Praesent consectetur, magna et bibendum fringilla, nunc mauris ornare odio, vel suscipit ante leo nec magna. Sed viverra in elit eu eleifend. Donec non maximus purus. Donec viverra ipsum non massa auctor, non auctor elit laoreet. Donec enim sapien, venenatis quis dui et, malesuada aliquet augue. Etiam suscipit neque in nunc aliquam lobortis. Aenean accumsan, enim nec gravida rhoncus, diam ligula congue dui, fringilla fringilla lectus lacus nec lacus. Cras scelerisque velit est, vel sagittis sapien aliquet sit amet. Vivamus cursus arcu eget arcu volutpat blandit. Duis imperdiet vel nibh id efficitur. Fusce varius diam eros, maximus sollicitudin nisl scelerisque non. Aenean placerat euismod elementum. Donec ac euismod elit, in placerat ex. Quisque et ex nibh.", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img5.jpg"}},
     {"id": 6, "title": "Post 6", "summary": "Summary to post 6 Summary to post 6 Summary to post 6","tags": ["tag4", "tag6"], "content": {"text": "Sample content for post 6.", "image": "https://storage.cloud.google.com/fastapi-python-be-test-uploads-folder/assets/img4.jpg"}},
]



origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Content(BaseModel):
    text: str
    image: str

class Post(BaseModel):
    id: int
    title: str = None
    summary: str = None
    tags: List[str] = []
    content: Content

@app.get("/")
def root():
    return {"details": f"Hello, world. This is my first prod!"}


#POSTS
@app.get("/posts", response_model=List[Post])
def list_posts(limit: int = 10):
    return dummy_posts[0:limit]

@app.post("/posts")
def create_post(post: Post):
    dummy_posts.append(post)
    return dummy_posts

@app.get("/posts/{id}", response_model=Post)
def get_post(id: int) -> Post:
    filtered_posts = [post for post in dummy_posts if post["id"] == id]
    if filtered_posts:
        return filtered_posts[0]
    else:
        raise HTTPException(status_code=404, detail=f"Post {id} not found")
    

@app.get("/posts/")
def get_posts_by_tags(tag: List[str] = Query(None)):
    if tag is None:
        return dummy_posts
    
    filtered_posts = [post for post in dummy_posts if any(t in post['tags'] for t in tag)]
    return filtered_posts