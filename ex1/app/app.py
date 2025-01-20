from flask import Flask
import redis
import psycopg2

app = Flask(__name__)

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

# Connect to PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        dbname="flask_db",
        user="admin",
        password="admin_pass",
        host="db"
    )
    return conn

@app.route('/')
def home():
    redis_client.set('message', 'Hello from Redis!')
    message = redis_client.get('message')
    return f"{message} \n Connected to PostgreSQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
