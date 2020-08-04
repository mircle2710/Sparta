from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# Read(조회) - 한 개 값만
movie = db.movies.find_one({'title': '월-E'})
print(movie['star'])

same_stars = list(db.movies.find({'star': movie['star']},{'_id': False}))
for same_star in same_stars:
    print(same_star['title'])
    db.movies.update_one({'title': same_star['title']}, {'$set': {'star': 0}})