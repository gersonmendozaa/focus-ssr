from flask import Flask
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379)

@app.route("/")
def welcome():
    cache.set('msg', 'Redis ON')
    print(cache.get('msg'))
    return "<h1>Hi from focus</h1>"

if __name__=="__main__":
    app.run(port=5000)