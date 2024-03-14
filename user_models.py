import requests
import pymysql.cursors
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create database connection pool
db_pool = None

def connect_db():
    global db_pool
    if not db_pool:
        db_pool = pymysql.connect(host=os.getenv('DB_HOST'),
                                   user=os.getenv('DB_USER'),
                                   password=os.getenv('DB_PASSWORD'),
                                   database=os.getenv('DB_DATABASE'),
                                   cursorclass=pymysql.cursors.DictCursor)
    return db_pool

def fetch_and_store_users():
    try:
        db = connect_db()
        app_id = os.getenv('APP_ID')

        # Make an HTTP request to fetch users' data from the API
        response = requests.get("https://dummyapi.io/data/v1/user", headers={"app-id": app_id})
        users = response.json().get('data', [])

        # Insert users' data into the MySQL database
        with db.cursor() as cursor:
            for user in users:
                email = user.get('email', '')  # Ensure email field is present or use empty string
                cursor.execute("INSERT INTO user (id, name, email) VALUES (%s, %s, %s)",
                               (user.get('id'), f"{user.get('firstName')} {user.get('lastName')}", email))
            db.commit()

        return True
    except Exception as e:
        print('Error fetching and storing users data:', e)
        return False

def fetch_and_store_posts_for_users():
    try:
        db = connect_db()

        # Fetch users list from the database
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM user')
            users = cursor.fetchall()

        # Iterate over the users list
        for user in users:
            # Make a request to the API to fetch corresponding posts data for the user
            response = requests.get(f"https://dummyapi.io/data/v1/user/{user['id']}/post",
                                    headers={"app-id": os.getenv('APP_ID')})
            posts = response.json().get('data', [])

            # Insert posts data into the database
            with db.cursor() as cursor:
                for post in posts:
                    cursor.execute("INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s)",
                                   (user['id'], post.get('title'), post.get('body')))
                db.commit()

        return True
    except Exception as e:
        print('Error fetching and storing posts data:', e)
        return False
