import json
from flask import Flask
import pymongo
from flask_caching import Cache 
import redis

app = Flask(__name__)

class BaseConfig(object):
    CACHE_TYPE='redis'
    CACHE_REDIS_HOST='redis'
    CACHE_REDIS_PORT='6379'
    CACHE_REDIS_DB='0'
    CACHE_REDIS_URL='redis://redis:6379/0'
    CACHE_DEFAULT_TIMEOUT='500'

    
app.config.from_object(BaseConfig)
cache = Cache(app)

buf = {}
myclient = pymongo.MongoClient("mongodb://db.local:27017/")
mydb = myclient["test_db"]
mycol = mydb["test_db"]
     
         
@app.route("/")
@cache.cached(timeout=30, query_string=True)
def home_page():
    for count, i in enumerate(mycol.find()):
        buf[count] = i
    return f'{buf}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
