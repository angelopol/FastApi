from pydantic import BaseModel
import pymysql
from datetime import datetime

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
    reaction1: int
    reaction2: int
    reaction3: int
    reaction4: int
    reaction5: int
    status: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def store(row):
        return Post(
            id=row[0],
            user=row[1],
            title=row[2],
            body=row[3],
            song=row[4],
            photo=row[5],
            bpm=row[6],
            scale=row[7],
            PaidMethods=row[8],
            cost=row[9],
            licenses=row[10],
            tags=row[11],
            reaction1=row[12],
            reaction2=row[13],
            reaction3=row[14],
            reaction4=row[15],
            reaction5=row[16],
            status=row[17],
            created_at=row[18],
            updated_at=row[19]
        )

def execute_query(query, get=True):
    try:
        connection = pymysql.connect(host='localhost', user='root', password='$0p0rt3', database='laravel')
        cursor = connection.cursor()
        cursor.execute(query)
        if get:
            return cursor.fetchall()
        else:
            connection.commit()
            return True
    except Exception as e:
        print(e)
        if get:
            return []
        else:
            return False

def get_posts():
    query = "SELECT * FROM posts"
    results = execute_query(query)
    return [Post.store(row) for row in results]

def get_post(id):
    query = f"SELECT * FROM posts WHERE id = {id}"
    result = execute_query(query)
    if result:
        return Post.store(result[0])
    return None

def create_post(post: Post):
    query = f"INSERT INTO posts (user, title, body, song, photo, bpm, scale, PaidMethods, cost, licenses, tags, reaction1, reaction2, reaction3, reaction4, reaction5, status, created_at, updated_at) VALUES ({post.user}, '{post.title}', '{post.body}', '{post.song}', '{post.photo}', {post.bpm}, '{post.scale}', '{post.PaidMethods}', {post.cost}, '{post.licenses}', '{post.tags}', '{post.reaction1}', '{post.reaction2}', '{post.reaction3}', '{post.reaction4}', '{post.reaction5}', {post.status}, '{post.created_at}', '{post.updated_at}')"
    return execute_query(query, False)

def update_post(id, post: Post):
    query = f"UPDATE posts SET user = {post.user}, title = '{post.title}', body = '{post.body}', song = '{post.song}', photo = '{post.photo}', bpm = {post.bpm}, scale = '{post.scale}', PaidMethods = '{post.PaidMethods}', cost = {post.cost}, licenses = '{post.licenses}', tags = '{post.tags}', reaction1 = '{post.reaction1}', reaction2 = '{post.reaction2}', reaction3 = '{post.reaction3}', reaction4 = '{post.reaction4}', reaction5 = '{post.reaction5}', status = {post.status}, created_at = '{post.created_at}', updated_at = '{post.updated_at}' WHERE id = {id}"
    return execute_query(query, False)

def delete_post(id):
    query = f"DELETE FROM posts WHERE id = {id}"
    return execute_query(query, False)