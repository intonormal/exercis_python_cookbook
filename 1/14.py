#你想排序类型相同的对象，但是他们不支持原生的比较操作。


from operator import attrgetter

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id
    def id(self):
        return self.user_id

print(User(23))

users = [User(23), User(3), User(99)]

print([item.id() for item in users])

sorted_user = sorted(users, key=attrgetter('user_id'))
print([item.id() for item in sorted_user])
