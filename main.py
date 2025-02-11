from fastapi import FastAPI, HTTPException
from post import Post, create_post, get_posts, get_post, update_post, delete_post

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Ruta para crear un nuevo post
@app.post("/posts/", response_model=Post)
async def store_post(post: Post):
    # Llamar a la función para crear un post
    create_post(post)
    # Devolver el post creado
    return post

# Ruta para obtener todos los posts
@app.get("/posts/", response_model=list[Post])
async def read_posts():
    # Llamar a la función para obtener todos los posts
    posts = get_posts()
    # Si no se encuentran posts, lanzar una excepción HTTP 404
    if len(posts) == 0:
        raise HTTPException(status_code=404, detail="No posts found")
    # Devolver la lista de posts
    return posts

# Ruta para obtener un post por su ID
@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int):
    # Llamar a la función para obtener un post por su ID
    post = get_post(post_id)
    # Si no se encuentra el post, lanzar una excepción HTTP 404
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    # Devolver el post encontrado
    return post

# Ruta para actualizar un post por su ID
@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    # Llamar a la función para actualizar un post
    update_post(post_id, post)
    # Devolver el post actualizado
    return post

# Ruta para eliminar un post por su ID
@app.delete("/posts/{post_id}", response_model=Post)
async def delete_post(post_id: int):
    # Llamar a la función para eliminar un post
    delete_post(post_id)
    # Devolver un mensaje de éxito
    return "Post deleted successfully"