from fastapi import FastAPI, HTTPException
from post import Post, create_post, get_posts, get_post, update_post, delete_post

app = FastAPI()

@app.post("/posts/", response_model=Post)
async def store_post(post: Post):
    create_post(post)
    return post

@app.get("/posts/", response_model=list[Post])
async def read_posts():
    posts = get_posts()
    if len(posts) == 0:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts

@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    update_post(post_id, post)
    return post

@app.delete("/posts/{post_id}", response_model=Post)
async def delete_post(post_id: int):
    delete_post(post_id)
    return "Post deleted successfully"