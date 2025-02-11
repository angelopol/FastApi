from pydantic import BaseModel
import pymysql

class Post(BaseModel):
    id: int
    user: int
    title: str
    body: str
    song: str
    photo: str
    bpm: float
    scale: str
    PaidMethods: str
    cost: float
    licenses: str
    tags: str
    reaction1: str
    reaction2: str
    reaction3: str
    reaction4: str
    reaction5: str
    status: int
    created_at: str
    updated_at: str

def execute_query(query, get=True):
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='$0p0rt3')
        cursor = connection.cursor()
        cursor.execute(query)
        if get:
            return cursor.fetchall()
        else:
            connection.commit()
            return True
    except Exception as e:
        print(e)
        return False
    
def get_posts():
    query = "SELECT * FROM posts"
    return execute_query(query)

def get_post(id):
    query = f"SELECT * FROM posts WHERE id = {id}"
    return execute_query(query)

def create_post(post: Post):
    query = f"INSERT INTO posts (user, title, body, song, photo, bpm, scale, PaidMethods, cost, licenses, tags, reaction1, reaction2, reaction3, reaction4, reaction5, status, created_at, updated_at) VALUES ({post.user}, '{post.title}', '{post.body}', '{post.song}', '{post.photo}', {post.bpm}, '{post.scale}', '{post.PaidMethods}', {post.cost}, '{post.licenses}', '{post.tags}', '{post.reaction1}', '{post.reaction2}', '{post.reaction3}', '{post.reaction4}', '{post.reaction5}', {post.status}, '{post.created_at}', '{post.updated_at}')"
    return execute_query(query, False)

def update_post(id, post: Post):
    query = f"UPDATE posts SET user = {post.user}, title = '{post.title}', body = '{post.body}', song = '{post.song}', photo = '{post.photo}', bpm = {post.bpm}, scale = '{post.scale}', PaidMethods = '{post.PaidMethods}', cost = {post.cost}, licenses = '{post.licenses}', tags = '{post.tags}', reaction1 = '{post.reaction1}', reaction2 = '{post.reaction2}', reaction3 = '{post.reaction3}', reaction4 = '{post.reaction4}', reaction5 = '{post.reaction5}', status = {post.status}, created_at = '{post.created_at}', updated_at = '{post.updated_at}' WHERE id = {id}"
    return execute_query(query, False)

def delete_post(id):
    query = f"DELETE FROM posts WHERE id = {id}"
    return execute_query(query, False)