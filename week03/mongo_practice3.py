from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
target_star = target_movie['star']

movies = list(db.movies.find({'star': target_star}))

for movie in movies:
    print(movie['title'])

    # # Create(생성)
    # user = {'name': '론', 'age': 40}
    # db.users.insert_one(user)
    #
    # # Read(조회) - 한 개 값만
    # user = db.users.find_one({'name': '론'})
    #
    # # Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
    # same_ages = list(db.users.find({'age': 40}, {'_id': False}))
    #
    # # Update(업데이트)
    # db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 116}})
    #
    # # Delete(삭제)
    # db.users.delete_one({'name': '론'})